package assignment2.groupXX.leader_election

import akka.actor.typed._
import akka.actor.typed.scaladsl._
import assignment2.groupXX.leader_election.Processor.{ProcessMessage, Wakeup}

object CoordinatingActor {

  trait CoordinatingMessage
  case class StartProcesses(nrProcesses : Int) extends CoordinatingMessage
  case class LeaderSelected(processName : String) extends CoordinatingMessage
  case class ProcessReady(processName : ActorRef[ProcessMessage]) extends CoordinatingMessage

  def apply(): Behaviors.Receive[CoordinatingMessage] = coordinate(Nil,Nil)

  def coordinate(processes : List[ActorRef[ProcessMessage]],
            readyProcesses : List[ActorRef[ProcessMessage]]) : Behaviors.Receive[CoordinatingMessage] = Behaviors.receive{
    (context, message) =>
      message match {
        case StartProcesses(nr) =>
          val processes = (0 until nr).map{i =>
            context.spawn(Processor.apply(context.self),name = s"process_$i")}
          println("Started actors")
          coordinate(processes.toList,Nil)
        case ProcessReady(process) =>
          // wait for all processes to be ready and then send out WakeUp messages
          ???
        case LeaderSelected(processName) =>
          // print that a leader has been selected and stop all actors
          ???
      }

  }

}
