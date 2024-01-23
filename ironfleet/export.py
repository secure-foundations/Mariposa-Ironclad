cmds = ["/arith:5 src/Dafny/Distributed/Common/Collections/Maps.i.dfy",
"/arith:5 src/Dafny/Distributed/Common/Collections/Maps2.i.dfy",
"src/Dafny/Distributed/Common/Collections/Maps2.s.dfy",
"src/Dafny/Distributed/Common/Collections/Seqs.s.dfy",
"/arith:5 src/Dafny/Distributed/Common/Collections/Sets.i.dfy",
"/arith:5 src/Dafny/Distributed/Common/Collections/Seqs.i.dfy",
"src/Dafny/Distributed/Common/Framework/AbstractService.s.dfy",
"src/Dafny/Distributed/Common/Framework/DistributedSystem.s.dfy",
"src/Dafny/Distributed/Common/Framework/Environment.s.dfy",
"src/Dafny/Distributed/Common/Framework/Host.s.dfy",
"src/Dafny/Distributed/Common/Framework/Main.s.dfy",
"/arith:5 src/Dafny/Distributed/Common/Logic/Option.i.dfy",
"src/Dafny/Distributed/Common/Logic/Temporal/Temporal.s.dfy",
"src/Dafny/Distributed/Common/Native/Io.s.dfy",
"/arith:5 src/Dafny/Distributed/Common/Native/NativeTypes.i.dfy",
"src/Dafny/Distributed/Common/Native/NativeTypes.s.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/CmdLineParser.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/GenericMarshalling.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/GenericRefinement.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/MarshallInt.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/NetClient.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/NodeIdentity.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/SeqIsUnique.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/SeqIsUniqueDef.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/Common/Util.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/CmdLineParser.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/Host.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/NetSHT.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/SchedulerImpl.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/SchedulerModel.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/LiveSHT/Unsendable.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/AppInterface.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/AppInterfaceConcrete.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/CMessage.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/ConstantsState.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/DelegationLookup.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/Delegations.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/HostModel.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/HostState.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/PacketParsing.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/Parameters.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/SHTConcreteConfiguration.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/SingleDeliveryModel.i.dfy",
"/arith:5 src/Dafny/Distributed/Impl/SHT/SingleDeliveryState.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/Common/NodeIdentity.i.dfy",
"src/Dafny/Distributed/Protocol/Common/NodeIdentity.s.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/Environment.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/EnvironmentLemmas.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/EnvironmentRefinement.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/SHT.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/SHTLemmas.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/SHTRefinement.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/SchedulerLemmas.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/RefinementProof/SchedulerRefinement.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/LiveSHT/Scheduler.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Configuration.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Delegations.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Host.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Keys.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Message.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Network.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/Parameters.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/RefinementProof/InvDefs.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/RefinementProof/InvProof.i.dfy",
"/arith:5 /noNLarith src/Dafny/Distributed/Protocol/SHT/RefinementProof/Refinement.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/RefinementProof/RefinementProof.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/RefinementProof/SHT.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/SingleDelivery.i.dfy",
"/arith:5 src/Dafny/Distributed/Protocol/SHT/SingleMessage.i.dfy",
"src/Dafny/Distributed/Services/SHT/AbstractService.s.dfy",
"/arith:5 src/Dafny/Distributed/Services/SHT/AppInterface.i.dfy",
"src/Dafny/Distributed/Services/SHT/AppInterface.s.dfy",
"src/Dafny/Distributed/Services/SHT/Bytes.s.dfy",
"src/Dafny/Distributed/Services/SHT/HT.s.dfy",
"/arith:5 src/Dafny/Distributed/Services/SHT/Main.i.dfy",
"/arith:5 src/Dafny/Distributed/Services/SHT/Marshall.i.dfy",
"/arith:5 src/Dafny/Distributed/Services/SHT/SHTDistributedSystem.i.dfy"]
# "/arith:5 src/Dafny/Libraries/Math/div.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/div_auto.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/div_auto_proofs.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/div_def.i.dfy",
# "/arith:2 src/Dafny/Libraries/Math/div_nonlinear.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/mod_auto.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/mod_auto_proofs.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/mul.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/mul_auto.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/mul_auto_proofs.i.dfy",
# "/arith:2 src/Dafny/Libraries/Math/mul_nonlinear.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/power.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/power2.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/power2s.i.dfy",
# "/arith:5 src/Dafny/Libraries/Math/powers.i.dfy"

import glob, os

# /vcsCores:4 

smt2_from_dfy = "dotnet /home/yizhou7/dafny/Dafny.dll /compile:0 /timeLimit:60 /functionSyntax:3 /deprecation:0 /proverLog:original/@FILE@.@PROC@.smt2 "

for i in range(len(cmds)):
    print("echo " + "\"" + cmds[i].split(" ")[-1] + "\"")
    print(smt2_from_dfy + cmds[i] + " /vcsCores:6 ")

bpl_from_dfy = "dotnet /home/yizhou7/dafny/Dafny.dll /compile:0 /functionSyntax:3 /deprecation:0 /noVerify "

smt2_from_bpl_prune = "dotnet boogie /prune /typeEncoding:a /emitDebugInformation:0 /proverLog:original/@FILE@.@PROC@.smt2 /timeLimit:1 "

smt2_from_bpl_bloat = "dotnet boogie /typeEncoding:a /emitDebugInformation:0 /proverLog:bloated/@FILE@.@PROC@.smt2 /timeLimit:1 "

# for cmd in cmds:
#     file = cmd.split(" ")[-1]
#     file = file.replace("/", "-").replace(".dfy", ".bpl")
#     print(bpl_from_dfy + " " + cmd + f" /print:boogies/{file}")

# print("echo \"run with parallel in bash\"")

# for bpl_file in glob.glob("boogies/*.bpl"):
#     print(smt2_from_bpl_prune + " " + bpl_file)
#     # print(smt2_from_bpl_bloat + " " + bpl_file)

# original = set([os.path.basename(f) for f in glob.glob("original/*.smt2")])
# bloated = set([os.path.basename(f) for f in glob.glob("bloated/*.smt2")])

# for file in glob.glob("bloated/*.smt2"):
#     new_content = []
#     for l in open(file):
#         new_content += [l]
#         if "(check-sat)" in l:
#             break
#     print(file)
#     open(file, "w").writelines(new_content)
