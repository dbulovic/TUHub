ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.8"

val AkkaVersion = "2.6.18"
libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor-typed" % AkkaVersion,
  "com.typesafe.akka" %% "akka-actor-testkit-typed" % AkkaVersion % Test
)
libraryDependencies +=
  "org.scalatest" %% "scalatest" % "3.2.9" % Test
libraryDependencies +=
  "ch.qos.logback" % "logback-classic" % "1.2.11"
lazy val root = (project in file("."))
  .settings(
    name := "assignment2"
  )
