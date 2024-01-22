include "../../Impl/LiveSHT/Host.i.dfy"
// include "../../Common/Framework/DistributedSystem.s.dfy"

module SHT_DistributedSystem_i {

    // import H_s = Host_i`All
import H_s  = Host_i`All
import opened Collections__Maps2_s
import opened Native__Io_s
import opened Environment_s
import opened Native__NativeTypes_s

/////////////////////////////////////////
// PHYSICAL ENVIRONMENT
/////////////////////////////////////////

predicate ValidPhysicalEnvironmentStep(step:LEnvStep<EndPoint, seq<byte>>)
{
  step.LEnvStepHostIos? ==> forall io{:trigger io in step.ios}{:trigger ValidPhysicalIo(io)} :: io in step.ios ==> ValidPhysicalIo(io)
}

/////////////////////////////////////////
// DS_State
/////////////////////////////////////////

datatype DS_State = DS_State(
  config:H_s.ConcreteConfiguration,
  environment:LEnvironment<EndPoint,seq<byte>>,
  servers:map<EndPoint,H_s.HostState>
  )

predicate DS_Init(s:DS_State, config:H_s.ConcreteConfiguration)
  reads *
{
  && s.config == config
  && H_s.ConcreteConfigToServers(s.config) == mapdomain(s.servers)
  && H_s.ConcreteConfigInit(s.config)
  && LEnvironment_Init(s.environment)
  && (forall id :: id in s.servers ==> H_s.HostInit(s.servers[id], config, id))
}
  
predicate DS_NextOneServer(s:DS_State, s':DS_State, id:EndPoint, ios:seq<LIoOp<EndPoint,seq<byte>>>)
  requires id in s.servers
  // reads *
{
  && id in s'.servers
  && H_s.HostNext(s.servers[id], s'.servers[id], ios)
  && s'.servers == s.servers[id := s'.servers[id]]
}

predicate DS_Next(s:DS_State, s':DS_State)
  // reads *
{
  && s'.config == s.config
  && LEnvironment_Next(s.environment, s'.environment)
  && ValidPhysicalEnvironmentStep(s.environment.nextStep)
  && if s.environment.nextStep.LEnvStepHostIos? && s.environment.nextStep.actor in s.servers then
      DS_NextOneServer(s, s', s.environment.nextStep.actor, s.environment.nextStep.ios)
    else
      s'.servers == s.servers
}
}
