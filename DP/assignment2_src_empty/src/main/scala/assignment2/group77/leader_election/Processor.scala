package assignment2.group77.leader_election

import akka.actor.typed._
import akka.actor.typed.scaladsl._
import assignment2.group77.leader_election.CoordinatingActor.{CoordinatingMessage, LeaderSelected,
  ProcessReady}

import scala.util.Random

object Processor {
  trait ProcessMessage
  case class Wakeup(nrProcesses : Int, nextProcess : ActorRef[ProcessMessage]) extends ProcessMessage
  case class Preference(value : Boolean) extends ProcessMessage
  case class Counter(value : Int) extends ProcessMessage

  def apply(parent : ActorRef[CoordinatingMessage]): Behavior[ProcessMessage] =
    Behaviors.setup[ProcessMessage]{
    context =>
      parent ! ProcessReady(context.self)
      idle(parent)
  }

  // use this function to generate random preferences
  def choosePreference() : Boolean = {
    new Random().nextBoolean()
  }

  def idle(parent : ActorRef[CoordinatingMessage])
  : Behaviors.Receive[ProcessMessage] = Behaviors.receive { (context, message) =>
    val name = context.self.path.name 
    message match {
      case Wakeup(nrProcesses, nextProcess) => context.log.info(name + " woken up")
        active(parent, nrProcesses, nextProcess, false, true)
      case Preference(value) => context.log.info(name + " not yet woken up")
                                idle(parent)
      case Counter(value) => context.log.info(name + " not yet woken up")
                             idle(parent)
    }
  }

  def active(parent : ActorRef[CoordinatingMessage], nrProcesses : Int, nextProcess : ActorRef[ProcessMessage], prevPref : Boolean, getNew : Boolean)
  : Behaviors.Receive[ProcessMessage] = {
    val currentPreference = if(getNew) choosePreference() else prevPref 
    if(getNew)
    {
      nextProcess ! Preference(currentPreference)
      nextProcess ! Counter(0)
    }

    Behaviors.receive { (context, message) =>
    val name = context.self.path.name 
    message match {
      case Preference(pref) => if(pref && !currentPreference)
                              {
                                context.log.info(f"$name%s is turning inactive")
                                inactive(parent, nextProcess)
                              } 
                              else active(parent, nrProcesses, nextProcess, currentPreference, true)
      case Counter(number) => if (number == nrProcesses - 1)
                              {
                                context.log.info(f"$name%s is the leader")
                                leader(parent, nextProcess, name) 
                              }
                            else active(parent, nrProcesses, nextProcess, currentPreference, false)
      case Wakeup(nrProcesses, nextProcess) => context.log.info(name + " already woken up")
                                                active(parent, nrProcesses, nextProcess, currentPreference, getNew)
                  }}
  }

  def inactive(parent : ActorRef[CoordinatingMessage], nextProcess : ActorRef[ProcessMessage])
  : Behaviors.Receive[ProcessMessage] = Behaviors.receive { (context, message) =>
    val name = context.self.path.name 
    message match {
      case Preference(value) => nextProcess ! Preference(value)
        inactive(parent, nextProcess)
      
      case Counter(value) => nextProcess ! Counter(value+1)
        inactive(parent, nextProcess)
      
      case Wakeup(nrProcesses, nextProcess) => context.log.info(name + " already woken up")
        inactive(parent, nextProcess)
    }
  }

  def leader(parent : ActorRef[CoordinatingMessage], nextProcess : ActorRef[ProcessMessage], name : String) : Behaviors.Receive[ProcessMessage] =
  {
    parent ! LeaderSelected(name)
    Behaviors.receive { (context, message) =>
    val name = context.self.path.name 
    message match {
      case Preference(value) => leader(parent, nextProcess, name)
      
      case Counter(value) => leader(parent, nextProcess, name)
      
      case Wakeup(nrProcesses, nextProcess) => context.log.info(name + " already woken up")
                                               leader(parent, nextProcess, name)
    }
  }
    
  }

}
