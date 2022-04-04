package assignment2.groupXX.leader_election

import akka.actor.typed._
import akka.actor.typed.scaladsl._
import assignment2.groupXX.leader_election.CoordinatingActor.{CoordinatingMessage, LeaderSelected,
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
    message match {
      case Wakeup(nrProcesses, nextProcess) => ???
    }
  }

}
