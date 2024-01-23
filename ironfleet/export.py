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

# bpl_from_dfy = "dotnet /home/yizhou7/dafny/Dafny.dll /compile:0 /functionSyntax:3 /deprecation:0 /noVerify "

# smt2_from_bpl_prune = "dotnet boogie /prune /typeEncoding:a /emitDebugInformation:0 /proverLog:original/@FILE@.@PROC@.smt2 /timeLimit:1 "

# smt2_from_bpl_bloat = "dotnet boogie /typeEncoding:a /emitDebugInformation:0 /proverLog:bloated/@FILE@.@PROC@.smt2 /timeLimit:1 "

# for cmd in cmds:
#     file = cmd.split(" ")[-1]
#     file = file.replace("/", "-").replace(".dfy", ".bpl")
#     print(bpl_from_dfy + " " + cmd + f" /print:boogies/{file}")

# print("echo \"run with parallel in bash\"")

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

def gen_bloat_script():
    smt2_from_bloat_dfy = "dotnet /home/yizhou7/dafny/BloatBinaries/Dafny.dll /compile:0 /timeLimit:60 /functionSyntax:3 /deprecation:0 /proverLog:bt/@FILE@.@PROC@.smt2 "
    f = open("bloat.sh", "w")
    f.write("#!/bin/bash\n")

    for i in range(len(cmds)):
        f.write("echo " + "\"" + cmds[i].split(" ")[-1] + "\"" + "\n")
        f.write(smt2_from_bloat_dfy + cmds[i] + " /vcsCores:6 \n")
    f.close()
    
    print("./bloat.sh | tee bloat.log.txt")

def gen_dfy_original_script():
    smt2_from_dfy = "dotnet /home/yizhou7/dafny/Binaries/Dafny.dll /compile:0 /timeLimit:60 /functionSyntax:3 /deprecation:0 /proverLog:or/@FILE@.@PROC@.smt2 "
    f = open("original.sh", "w")
    f.write("#!/bin/bash\n")

    for i in range(len(cmds)):
        f.write("echo " + "\"" + cmds[i].split(" ")[-1] + "\"" + "\n")
        f.write(smt2_from_dfy + cmds[i] + " /vcsCores:6 \n")
    f.close()

    print("./original.sh | tee original.log.txt")

def get_files(subdir):
    files = set()
    for smt2 in glob.glob(subdir + "/*.smt2"):
        files.add(os.path.basename(smt2))
    return files

def read_log(log_file):
    import re
    verified = re.compile("([0-9]+) verified")
    errors = re.compile("([0-9]+) error")
    timeouts = re.compile("([0-9]+) time out")
    counts = {"verified": 0, "errors": 0, "timeouts": 0}
    for line in open(log_file).readlines():
        v_match = verified.search(line)
        e_match = errors.search(line)
        t_match = timeouts.search(line)
        if v_match:
            # print(v_match.group(1), end=" ")
            counts["verified"] += int(v_match.group(1))
        if e_match:
            # print(e_match.group(1), end=" ")
            if int(e_match.group(1)) > 0:
                print(line)
            counts ["errors"] +=  int(e_match.group(1))
        if t_match:
            if int(e_match.group(1)) > 0:
                print(line)
            # print(t_match.group(1), end=" ")
            counts["timeouts"] += int(t_match.group(1))
    print(counts)

# read_log("original.log.txt")
# read_log("bloat.log.txt")

def match_files():
    org = get_files("or")
    blt = get_files("bt") 

    bloated_ = blt - org
    original_ = org - blt

    # import editdistance

    # new_names = set()
    # count = 0
    # not_matched = set()
    # for b in bloated_:
    #     scores = []
    #     for o in original_:
    #         scores.append((o, editdistance.eval(b, o)))
    #     min_score = min(scores, key=lambda x: x[1])
    #     # if max is unique then rename
    #     if len([s for s in scores if s[1] == min_score[1]]) == 1:
    #         print(b)
    #         print(min_score[0])
    #         print("")
    #         new_names.add(min_score[0])
    #         os.rename("bloated/" + b, "bloated/" + min_score[0])
    #         count += 1
    #     else:
    #         not_matched.add(b)

    # print("")
    # for j in not_matched:
    #     print(j)
    # print("")
    # for k in original_ - new_names:
    #     print(k)

def process_smt2_basic():
    subdir = "or"
    for smt2 in glob.glob(subdir + "/*.smt2"):
        new_content = []
        for line in open(smt2).readlines():
            new_content.append(line)
            if "(check-sat)" in line:
                break
        open(smt2, "w").writelines(new_content)
        print(smt2)
        # break
    
process_smt2_basic()
# print(len(new_names))
# print(count)
