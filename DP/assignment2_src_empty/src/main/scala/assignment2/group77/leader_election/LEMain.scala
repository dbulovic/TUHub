package assignment2.group77.leader_election

import akka.actor.typed.ActorSystem
import assignment2.group77.leader_election.CoordinatingActor.StartProcesses

object LEMain extends App {

  // initialise your actor system here
  val coordinator: ActorSystem[CoordinatingActor.CoordinatingMessage] = ActorSystem(CoordinatingActor(), "Coordinator")

  println("\n" ++ "Coordinator Actor started." ++ "\n")

  coordinator ! CoordinatingActor.StartProcesses(99)

}
