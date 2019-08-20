""" File: HMLLDBClassInfo.py

An lldb Python script to print infomation of lldb class.(In order to learn)

"""

import lldb


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand(
        'command script add -f HMLLDBClassInfo.plldbClassInfo plldbClassInfo -h "Print infomation of lldb class."')


gLastCommand = ""  # List of module names that may be user-written


def plldbClassInfo(debugger, command, exe_ctx, result, internal_dict):
    """
    Syntax:
        plldbClassInfo <className>

    Examples:
        (lldb) plldbClassInfo all
        (lldb) plldbClassInfo SBTarget
        (lldb) plldbClassInfo SBValue

    This command is implemented in HMLLDBClassInfo.py
    """
    if len(command) == 0:
        print ("Error input, plase input 'help plldbClassInfo' for more infomation")
        return

    global gLastCommand
    gLastCommand = command

    if compareName("SBDebugger"):
        pSBDebugger()
    if compareName("SBTarget"):
        pSBTarget()
    if compareName("SBProcess"):
        pSBProcess()
    if compareName("SBProcessInfo"):
        pSBProcessInfo()
    if compareName("SBThread"):
        pSBThread()
    if compareName("SBFrame"):
        pSBFrame()

    if compareName("SBPlatform"):
        pSBPlatform()
    if compareName("SBCommandInterpreter"):
        pSBCommandInterpreter()
    if compareName("SBBreakpoint"):
        pSBBreakpoint()
    if compareName("SBFileSpec"):
        pSBFileSpec()
    if compareName("SBSymbolContext"):
        pSBSymbolContext()
    if compareName("SBSymbol"):
        pSBSymbol()

    if compareName("SBType"):
        pSBType()
    if compareName("SBTypeMemberFunction"):
        pSBTypeMemberFunction()

    if compareName("SBListener"):
        pSBListener()
    if compareName("SBTypeCategory"):
        pSBTypeCategory()
    if compareName("SBSourceManager"):
        pSBSourceManager()
    if compareName("SBStructuredData"):
        pSBStructuredData()
    if compareName("SBUnixSignals"):
        pSBUnixSignals()
    if compareName("SBBroadcaster"):
        pSBBroadcaster()
    if compareName("SBLaunchInfo"):
        pSBLaunchInfo()


def compareName(className):
    global gLastCommand
    if gLastCommand.lower() in className.lower() or gLastCommand.lower() == "all":
        return True
    else:
        return False


def printFormat(desc, value):
    print ("[{arg1}]: {arg2}\n\ttype: {arg3}".format(arg1=desc, arg2=value, arg3=type(value)))


def printClassName(title):
    print ("\n\n====={arg1}================================".format(arg1=title))


def printTraversal(obj, getsize, getelem):
    print ("\n##### [{arg1}] #####".format(arg1=getelem))
    size = getattr(obj, getsize)
    elem = getattr(obj, getelem)
    for i in range(size()):
        if i == 0:
            print (type(elem(i)))
        print (elem(i))


def pSBDebugger():
    debugger = lldb.debugger

    printClassName("SBDebugger")
    printFormat("SBDebugger", debugger)
    printFormat("IsValid", debugger.IsValid())
    printFormat("GetAsync", debugger.GetAsync())
    printFormat("GetInputFileHandle", debugger.GetInputFileHandle())  # FILE
    printFormat("GetOutputFileHandle", debugger.GetOutputFileHandle())  # FILE
    printFormat("GetErrorFileHandle", debugger.GetErrorFileHandle())  # FILE
    printFormat("GetCommandInterpreter", debugger.GetCommandInterpreter())  # SBCommandInterpreter
    printFormat("GetListener", debugger.GetListener())  # SBListener
    printFormat("GetDummyTarget", debugger.GetDummyTarget())  # SBTarget
    printFormat("GetNumTargets", debugger.GetNumTargets())
    printFormat("GetSelectedTarget", debugger.GetSelectedTarget())  # SBTarget
    printFormat("GetSelectedPlatform", debugger.GetSelectedPlatform())  # GetSelectedPlatform
    printFormat("GetNumPlatforms", debugger.GetNumPlatforms())
    printFormat("GetNumAvailablePlatforms", debugger.GetNumAvailablePlatforms())
    printFormat("GetSourceManager", debugger.GetSourceManager())  # SBSourceManager
    printFormat("GetUseExternalEditor", debugger.GetUseExternalEditor())
    printFormat("GetUseColor", debugger.GetUseColor())
    printFormat("GetVersionString", debugger.GetVersionString())
    printFormat("GetBuildConfiguration", debugger.GetBuildConfiguration())  # SBStructuredData
    printFormat("GetInstanceName", debugger.GetInstanceName())
    printFormat("GetTerminalWidth", debugger.GetTerminalWidth())
    printFormat("GetID", debugger.GetID())
    printFormat("GetPrompt", debugger.GetPrompt())
    printFormat("GetScriptLanguage", debugger.GetScriptLanguage())  # ScriptLanguage int
    printFormat("GetCloseInputOnEOF", debugger.GetCloseInputOnEOF())
    printFormat("GetNumCategories", debugger.GetNumCategories())
    printFormat("GetDefaultCategory", debugger.GetDefaultCategory())  # SBTypeCategory

    printTraversal(debugger, "GetNumTargets", "GetTargetAtIndex")  # [SBTarget]
    printTraversal(debugger, "GetNumPlatforms", "GetPlatformAtIndex")  # [SBPlatform]
    printTraversal(debugger, "GetNumCategories", "GetCategoryAtIndex")  # [SBTypeCategory]


def pSBTarget():
    target = lldb.debugger.GetSelectedTarget()

    printClassName("SBTarget")
    printFormat("SBTarget", target)
    printFormat("IsValid", target.IsValid())
    printFormat("GetBroadcasterClassName", target.GetBroadcasterClassName())
    printFormat("GetProcess", target.GetProcess())  # SBProcess
    printFormat("GetPlatform", target.GetPlatform())  # SBPlatform
    printFormat("GetExecutable", target.GetExecutable())  # SBFileSpec
    printFormat("GetNumModules", target.GetNumModules())
    printFormat("GetDebugger", target.GetDebugger())  # SBDebugger
    printFormat("GetByteOrder", target.GetByteOrder())  # ByteOrder int
    printFormat("GetAddressByteSize", target.GetAddressByteSize())
    printFormat("GetTriple", target.GetTriple())
    printFormat("GetDataByteSize", target.GetDataByteSize())
    printFormat("GetCodeByteSize", target.GetCodeByteSize())
    printFormat("FindFunctions.first", target.FindFunctions("viewDidLoad")[0])  # SBSymbolContext
    printFormat("FindFirstType", target.FindFirstType("UIAlertAction"))  # SBType
    printFormat("FindTypes", target.FindTypes("UIAlertAction"))  # SBTypeList
    printFormat("GetSourceManager", target.GetSourceManager())  # SBSourceManager
    printFormat("FindFirstGlobalVariable", target.FindFirstGlobalVariable("shared"))  # SBValue
    printFormat("FindGlobalVariables", target.FindGlobalVariables("shared", 2))  # SBValueList
    printFormat("FindGlobalFunctions.first", target.FindGlobalFunctions("viewDidLoad", 1, 0)[0])  # SBSymbolContext
    printFormat("GetNumBreakpoints", target.GetNumBreakpoints())
    printFormat("GetNumWatchpoints", target.GetNumWatchpoints())
    printFormat("GetBroadcaster", target.GetBroadcaster())  # SBBroadcaster
    printFormat("FindSymbols", target.FindSymbols("UIAlertAction"))  # SBSymbolContextList
    printFormat("GetStackRedZoneSize", target.GetStackRedZoneSize())
    printFormat("GetLaunchInfo", target.GetLaunchInfo())  # SBLaunchInfo
    printFormat("GetCollectingStats", target.GetCollectingStats())
    printFormat("GetStatistics", target.GetStatistics())  # SBStructuredData

    printTraversal(target, "GetNumModules", "GetModuleAtIndex")  # [SBModule]
    printTraversal(target, "GetNumBreakpoints", "GetBreakpointAtIndex")  # [SBBreakpoint]
    printTraversal(target, "GetNumWatchpoints", "GetWatchpointAtIndex")  # [SBWatchpoint]


def pSBProcess():
    process = lldb.debugger.GetSelectedTarget().GetProcess()
    # process = lldb.debugger.GetCommandInterpreter().GetProcess()

    printClassName("SBProcess")
    printFormat("SBProcess", process)
    printFormat("GetBroadcasterClassName", process.GetBroadcasterClassName())
    printFormat("GetPluginName", process.GetPluginName())
    printFormat("GetShortPluginName", process.GetShortPluginName())
    printFormat("IsValid", process.IsValid())
    printFormat("GetTarget", process.GetTarget())  # SBTarget
    printFormat("GetByteOrder", process.GetByteOrder())  # ByteOrder int
    printFormat("GetNumThreads", process.GetNumThreads())
    printFormat("GetSelectedThread", process.GetSelectedThread())  # SBThread
    printFormat("GetNumQueues", process.GetNumQueues())
    printFormat("GetState", process.GetState())  # StateType int
    printFormat("GetExitStatus", process.GetExitStatus())
    printFormat("GetExitDescription", process.GetExitDescription())
    printFormat("GetProcessID", process.GetProcessID())
    printFormat("GetUniqueID", process.GetUniqueID())
    printFormat("GetAddressByteSize", process.GetAddressByteSize())
    printFormat("GetUnixSignals", process.GetUnixSignals())  # SBUnixSignals
    printFormat("GetBroadcaster", process.GetBroadcaster())  # SBBroadcaster
    printFormat("GetNumExtendedBacktraceTypes", process.GetNumExtendedBacktraceTypes())
    printFormat("GetMemoryRegions", process.GetMemoryRegions())  # SBMemoryRegionInfoList
    printFormat("GetProcessInfo", process.GetProcessInfo())  # SBProcessInfo
    printFormat("__get_is_alive__", process.__get_is_alive__())
    printFormat("__get_is_running__", process.__get_is_running__())
    printFormat("__get_is_stopped__", process.__get_is_stopped__())

    printTraversal(process, "GetNumThreads", "GetThreadAtIndex")  # [SBThread]
    printTraversal(process, "GetNumQueues", "GetQueueAtIndex")  # [SBQueue]
    printTraversal(process, "GetNumExtendedBacktraceTypes", "GetExtendedBacktraceTypeAtIndex")  # [str]


def pSBProcessInfo():
    info = lldb.debugger.GetSelectedTarget().GetProcess().GetProcessInfo()

    printClassName("SBProcessInfo")
    printFormat("SBProcessInfo", info)
    printFormat("IsValid", info.IsValid())
    printFormat("GetName", info.GetName())
    printFormat("GetExecutableFile", info.GetExecutableFile())  # SBFileSpec
    printFormat("GetProcessID", info.GetProcessID())
    printFormat("GetUserID", info.GetUserID())
    printFormat("GetGroupID", info.GetGroupID())
    printFormat("UserIDIsValid", info.UserIDIsValid())
    printFormat("GroupIDIsValid", info.GroupIDIsValid())
    printFormat("GetEffectiveUserID", info.GetEffectiveUserID())
    printFormat("GetEffectiveGroupID", info.GetEffectiveGroupID())
    printFormat("EffectiveUserIDIsValid", info.EffectiveUserIDIsValid())
    printFormat("EffectiveGroupIDIsValid", info.EffectiveGroupIDIsValid())
    printFormat("GetParentProcessID", info.GetParentProcessID())


def pSBThread():
    thread = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread()

    printClassName("SBThread")
    printFormat("SBThread", thread)
    printFormat("GetBroadcasterClassName", thread.GetBroadcasterClassName())
    printFormat("IsValid", thread.IsValid())
    printFormat("GetStopReason", thread.GetStopReason())  # StopReason int
    printFormat("GetStopReasonDataCount", thread.GetStopReasonDataCount())
    printFormat("GetStopReturnValue", thread.GetStopReturnValue())  # SBValue
    printFormat("GetStopErrorValue", thread.GetStopErrorValue())  # SBValue
    printFormat("GetThreadID", thread.GetThreadID())
    printFormat("GetIndexID", thread.GetIndexID())
    printFormat("GetName", thread.GetName())
    printFormat("GetQueueName", thread.GetQueueName())
    printFormat("GetQueueID", thread.GetQueueID())
    printFormat("GetQueue", thread.GetQueue())  # SBQueue
    printFormat("IsSuspended", thread.IsSuspended())
    printFormat("IsStopped", thread.IsStopped())
    printFormat("GetNumFrames", thread.GetNumFrames())
    printFormat("GetSelectedFrame", thread.GetSelectedFrame())  # SBFrame
    printFormat("GetProcess", thread.GetProcess())  # SBProcess
    printFormat("SafeToCallFunctions", thread.SafeToCallFunctions())

    printTraversal(thread, "GetStopReasonDataCount", "GetStopReasonDataAtIndex")  # [int]
    printTraversal(thread, "GetNumFrames", "GetFrameAtIndex")  # [SBFrame]


def pSBFrame():
    frame = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame()

    printClassName("SBFrame")
    printFormat("SBFrame", frame)
    printFormat("IsValid", frame.IsValid())
    printFormat("GetFrameID", frame.GetFrameID())
    printFormat("GetCFA", frame.GetCFA())
    printFormat("GetPC", frame.GetPC())
    printFormat("GetSP", frame.GetSP())
    printFormat("GetFP", frame.GetFP())
    printFormat("GetPCAddress", frame.GetPCAddress())  # SBAddress
    printFormat("GetSymbolContext", frame.GetSymbolContext(lldb.eSymbolContextEverything))  # SBSymbolContext
    printFormat("GetModule", frame.GetModule())  # SBModule
    printFormat("GetCompileUnit", frame.GetCompileUnit())  # SBCompileUnit
    printFormat("GetFunction", frame.GetFunction())  # SBFunction
    printFormat("GetSymbol", frame.GetSymbol())  # SBSymbol
    printFormat("GetBlock", frame.GetBlock())  # SBBlock
    printFormat("GetDisplayFunctionName", frame.GetDisplayFunctionName())
    printFormat("GetFunctionName", frame.GetFunctionName())
    printFormat("GuessLanguage", frame.GuessLanguage())  # LanguageType int
    printFormat("IsSwiftThunk", frame.IsSwiftThunk())
    printFormat("IsInlined", frame.IsInlined())
    printFormat("IsArtificial", frame.IsArtificial())
    printFormat("GetFrameBlock", frame.GetFrameBlock())  # SBBlock
    printFormat("GetLineEntry", frame.GetLineEntry())  # SBLineEntry
    printFormat("GetThread", frame.GetThread())  # SBThread
    printFormat("Disassemble", frame.Disassemble())

    printFormat("GetVariables", frame.GetVariables(True, True, True, False))  # SBValueList
    # printFormat("get_arguments", frame.get_arguments())  # SBValueList
    # printFormat("get_locals", frame.get_locals())  # SBValueList
    # printFormat("get_statics", frame.get_statics())  # SBValueList

    printFormat("GetRegisters", frame.GetRegisters())  # SBValueList
    printFormat("FindVariable", frame.FindVariable("self"))  # SBValue
    printFormat("GetValueForVariablePath", frame.GetValueForVariablePath("self.customVariable"))  # SBValue
    printFormat("get_parent_frame", frame.get_parent_frame())  # SBFrame


def pSBValue():
    # TODO
    value = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().FindVariable("self")


def pSBQueue():
    # TODO
    queue = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetQueue()
    # queue = lldb.debugger.GetSelectedTarget().GetProcess().GetQueueAtIndex(0)


def pSBSymbolContext():
    ctx = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetSymbolContext(lldb.eSymbolContextEverything)
    # ctx = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0]

    printClassName("SBSymbolContext")
    printFormat("SBSymbolContext", ctx)
    printFormat("IsValid", ctx.IsValid())
    printFormat("GetModule", ctx.GetModule())  # SBModule
    printFormat("GetCompileUnit", ctx.GetCompileUnit())  # SBCompileUnit
    printFormat("GetFunction", ctx.GetFunction())  # SBFunction
    printFormat("GetBlock", ctx.GetBlock())  # SBBlock
    printFormat("GetLineEntry", ctx.GetLineEntry())  # SBLineEntry
    printFormat("GetSymbol", ctx.GetSymbol())  # SBSymbol


def pSBSymbol():
    symbol = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetSymbol()
    # symbol = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetSymbol()

    printClassName("SBSymbol")
    printFormat("SBSymbol", symbol)
    printFormat("IsValid", symbol.IsValid())
    printFormat("GetName", symbol.GetName())
    printFormat("GetDisplayName", symbol.GetDisplayName())
    printFormat("GetMangledName", symbol.GetMangledName())
    printFormat("GetStartAddress", symbol.GetStartAddress())  # SBAddress
    printFormat("GetEndAddress", symbol.GetEndAddress())  # SBAddress
    printFormat("GetPrologueByteSize", symbol.GetPrologueByteSize())
    printFormat("GetType", symbol.GetType())  # SymbolType int
    printFormat("IsExternal", symbol.IsExternal())
    printFormat("IsSynthetic", symbol.IsSynthetic())
    printFormat("GetInstructions", symbol.GetInstructions(lldb.debugger.GetSelectedTarget()))  # SBInstructionList


def pSBModule():
    # TODO
    module = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetModule()
    module = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetModule()


def pSBCompileUnit():
    # TODO
    cu = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetCompileUnit()
    cu = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetCompileUnit()


def pSBFunction():
    # TODO
    func = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetFunction()
    func = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetFunction()


def pSBBlock():
    # TODO
    b = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetBlock()
    b = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetBlock()
    b = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetFrameBlock()


def pSBLineEntry():
    # TODO
    le = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetLineEntry()
    le = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetLineEntry()


def pSBAddress():
    # TODO
    address = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetSymbol().GetStartAddress()
    # address = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetSymbol().GetEndAddress()
    # address = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame().GetPCAddress()


def pSBInstructionList():
    # TODO
    instructionList = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")[0].GetSymbol().GetInstructions(lldb.debugger.GetSelectedTarget())


def pSBType():
    t = lldb.debugger.GetSelectedTarget().FindFirstType("UIAlertAction")

    printClassName("SBType")
    printFormat("SBType", t)
    printFormat("IsValid", t.IsValid())
    printFormat("GetByteSize", t.GetByteSize())
    printFormat("IsPointerType", t.IsPointerType())
    printFormat("IsReferenceType", t.IsReferenceType())
    printFormat("IsFunctionType", t.IsFunctionType())
    printFormat("IsPolymorphicClass", t.IsPolymorphicClass())
    printFormat("IsArrayType", t.IsArrayType())
    printFormat("IsVectorType", t.IsVectorType())
    printFormat("IsTypedefType", t.IsTypedefType())
    printFormat("IsAnonymousType", t.IsAnonymousType())
    printFormat("GetPointerType", t.GetPointerType())  # SBType
    printFormat("GetPointeeType", t.GetPointeeType())  # SBType
    printFormat("GetReferenceType", t.GetReferenceType())  # SBType
    printFormat("GetTypedefedType", t.GetTypedefedType())  # SBType
    printFormat("GetDereferencedType", t.GetDereferencedType())  # SBType
    printFormat("GetUnqualifiedType", t.GetUnqualifiedType())  # SBType
    printFormat("GetCanonicalType", t.GetCanonicalType())  # SBType
    printFormat("GetArrayElementType", t.GetArrayElementType())  # SBType
    printFormat("GetVectorElementType", t.GetVectorElementType())  # SBType
    printFormat("GetBasicType", t.GetBasicType())  # BasicType int
    printFormat("GetNumberOfFields", t.GetNumberOfFields())
    printFormat("GetNumberOfDirectBaseClasses", t.GetNumberOfDirectBaseClasses())
    printFormat("GetNumberOfVirtualBaseClasses", t.GetNumberOfVirtualBaseClasses())
    printFormat("GetEnumMembers", t.GetEnumMembers())  # SBTypeEnumMemberList
    printFormat("GetName", t.GetName())
    printFormat("GetDisplayTypeName", t.GetDisplayTypeName())
    printFormat("GetTypeClass", t.GetTypeClass())  # TypeClass int
    printFormat("GetNumberOfTemplateArguments", t.GetNumberOfTemplateArguments())
    printFormat("GetFunctionReturnType", t.GetFunctionReturnType())  # SBType
    printFormat("GetFunctionArgumentTypes", t.GetFunctionArgumentTypes())  # SBTypeList
    printFormat("GetNumberOfMemberFunctions", t.GetNumberOfMemberFunctions())
    printFormat("IsTypeComplete", t.IsTypeComplete())
    printFormat("GetTypeFlags", t.GetTypeFlags())

    printTraversal(t, "GetNumberOfFields", "GetFieldAtIndex")  # [SBTypeMember]
    printTraversal(t, "GetNumberOfDirectBaseClasses", "GetDirectBaseClassAtIndex")  # [SBTypeMember]
    printTraversal(t, "GetNumberOfVirtualBaseClasses", "GetVirtualBaseClassAtIndex")  # [SBTypeMember]
    printTraversal(t, "GetNumberOfTemplateArguments", "GetTemplateArgumentType")  # [SBType]
    printTraversal(t, "GetNumberOfMemberFunctions", "GetMemberFunctionAtIndex")  # [SBTypeMemberFunction]


def pSBTypeMemberFunction():
    func = lldb.debugger.GetSelectedTarget().FindFirstType("UIAlertAction").GetMemberFunctionAtIndex(0)

    printClassName("SBTypeMemberFunction")
    printFormat("SBTypeMemberFunction", func)
    printFormat("IsValid", func.IsValid())
    printFormat("GetName", func.GetName())
    printFormat("GetDemangledName", func.GetDemangledName())
    printFormat("GetMangledName", func.GetMangledName())
    printFormat("GetType", func.GetType())  # SBType
    printFormat("GetReturnType", func.GetReturnType())  # SBType
    printFormat("GetNumberOfArguments", func.GetNumberOfArguments())
    printFormat("GetKind", func.GetKind())  # MemberFunctionKind int

    printTraversal(func, "GetNumberOfArguments", "GetArgumentTypeAtIndex")  # [SBType]


def pSBFileSpec():
    fileSpec = lldb.debugger.GetSelectedTarget().GetExecutable()
    # fileSpec = lldb.debugger.GetSelectedTarget().GetLaunchInfo().GetExecutableFile()
    # fileSpec = lldb.debugger.GetSelectedTarget().GetProcess().GetProcessInfo().GetExecutableFile()

    printClassName("SBFileSpec")
    printFormat("SBFileSpec", fileSpec)
    printFormat("IsValid", fileSpec.IsValid())
    printFormat("Exists", fileSpec.Exists())
    printFormat("ResolveExecutableLocation", fileSpec.ResolveExecutableLocation())
    printFormat("GetFilename", fileSpec.GetFilename())
    printFormat("GetDirectory", fileSpec.GetDirectory())
    printFormat("fullpath", fileSpec.fullpath)


def pSBBreakpoint():
    bp = lldb.debugger.GetSelectedTarget().GetBreakpointAtIndex(0)

    printClassName("SBBreakpoint")
    printFormat("SBBreakpoint", bp)
    printFormat("GetID", bp.GetID())
    printFormat("IsValid", bp.IsValid())
    printFormat("IsEnabled", bp.IsEnabled())
    printFormat("IsOneShot", bp.IsOneShot())
    printFormat("IsInternal", bp.IsInternal())
    printFormat("GetHitCount", bp.GetHitCount())
    printFormat("GetIgnoreCount", bp.GetIgnoreCount())
    printFormat("GetCondition", bp.GetCondition())
    printFormat("GetAutoContinue", bp.GetAutoContinue())
    printFormat("GetThreadID", bp.GetThreadID())
    printFormat("GetThreadIndex", bp.GetThreadIndex())
    printFormat("GetThreadName", bp.GetThreadName())
    printFormat("GetQueueName", bp.GetQueueName())
    printFormat("GetNumLocations", bp.GetNumLocations())
    printFormat("IsHardware", bp.IsHardware())

    printTraversal(bp, "GetNumLocations", "GetLocationAtIndex")  # [SBBreakpointLocation]


def pSBPlatform():
    platform = lldb.debugger.GetSelectedPlatform()
    # platform = lldb.debugger.GetSelectedTarget().GetPlatform()

    printClassName("SBPlatform")
    printFormat("SBPlatform", platform)
    printFormat("IsValid", platform.IsValid())
    printFormat("GetWorkingDirectory", platform.GetWorkingDirectory())
    printFormat("GetName", platform.GetName())
    printFormat("IsConnected", platform.IsConnected())
    printFormat("GetTriple", platform.GetTriple())
    printFormat("GetHostname", platform.GetHostname())
    printFormat("GetOSBuild", platform.GetOSBuild())
    printFormat("GetOSDescription", platform.GetOSDescription())
    printFormat("GetOSMajorVersion", platform.GetOSMajorVersion())
    printFormat("GetOSMinorVersion", platform.GetOSMinorVersion())
    printFormat("GetOSUpdateVersion", platform.GetOSUpdateVersion())
    printFormat("GetUnixSignals", platform.GetUnixSignals())  # SBUnixSignals


def pSBCommandInterpreter():
    ci = lldb.debugger.GetCommandInterpreter()

    printClassName("SBCommandInterpreter")
    printFormat("SBCommandInterpreter", ci)
    printFormat("IsValid", ci.IsValid())
    printFormat("GetPromptOnQuit", ci.GetPromptOnQuit())
    printFormat("HasCustomQuitExitCode", ci.HasCustomQuitExitCode())
    printFormat("GetQuitStatus", ci.GetQuitStatus())
    printFormat("CommandExists", ci.CommandExists("breakpoint"))
    printFormat("AliasExists", ci.AliasExists('bt'))
    printFormat("GetBroadcaster", ci.GetBroadcaster())  # SBBroadcaster
    printFormat("GetBroadcasterClass", ci.GetBroadcasterClass())
    printFormat("HasCommands", ci.HasCommands())
    printFormat("HasAliases", ci.HasAliases())
    printFormat("HasAliasOptions", ci.HasAliasOptions())
    printFormat("GetProcess", ci.GetProcess())  # SBProcess
    printFormat("GetDebugger", ci.GetDebugger())  # SBDebugger
    printFormat("IsActive", ci.IsActive())
    printFormat("WasInterrupted", ci.WasInterrupted())


def pSBSourceManager():
    manager = lldb.debugger.GetSourceManager()
    # manager = lldb.debugger.GetSelectedTarget().GetSourceManager()

    printClassName("SBSourceManager")
    printFormat("SBSourceManager", manager)


def pSBStructuredData():
    sd = lldb.debugger.GetBuildConfiguration()
    # sd = lldb.debugger.GetSelectedTarget().GetStatistics()

    printClassName("SBStructuredData")
    printFormat("SBStructuredData", sd)
    printFormat("IsValid", sd.IsValid())
    printFormat("GetType", sd.GetType())  # StructuredDataType int
    printFormat("GetSize", sd.GetSize())
    printFormat("GetIntegerValue", sd.GetIntegerValue())
    printFormat("GetFloatValue", sd.GetFloatValue())
    printFormat("GetBooleanValue", sd.GetBooleanValue())


def pSBTypeCategory():
    category = lldb.debugger.GetDefaultCategory()

    printClassName("SBTypeCategory")
    printFormat("SBTypeCategory", category)
    printFormat("IsValid", category.IsValid())
    printFormat("GetEnabled", category.GetEnabled())
    printFormat("GetName", category.GetName())
    printFormat("GetNumLanguages", category.GetNumLanguages())
    printFormat("GetNumFormats", category.GetNumFormats())
    printFormat("GetNumSummaries", category.GetNumSummaries())
    printFormat("GetNumFilters", category.GetNumFilters())
    printFormat("GetNumSynthetics", category.GetNumSynthetics())

    printTraversal(category, "GetNumLanguages", "GetLanguageAtIndex")  # [LanguageType] [int]
    printTraversal(category, "GetNumFormats", "GetFormatAtIndex")  # [SBTypeFormat]
    printTraversal(category, "GetNumSummaries", "GetSummaryAtIndex")  # [SBTypeSummary]
    printTraversal(category, "GetNumFilters", "GetFilterAtIndex")  # [SBTypeFilter]
    printTraversal(category, "GetNumSynthetics", "GetSyntheticAtIndex")  # [SBTypeSynthetic]


def pSBUnixSignals():
    signals = lldb.debugger.GetSelectedPlatform().GetUnixSignals()
    # signals = lldb.debugger.GetSelectedTarget().GetProcess().GetUnixSignals()

    printClassName("SBUnixSignals")
    printFormat("SBUnixSignals", signals)
    printFormat("IsValid", signals.IsValid())
    printFormat("GetNumSignals", signals.GetNumSignals())

    printTraversal(signals, "GetNumSignals", "GetSignalAtIndex")  # [int]


def pSBBroadcaster():
    broadcaster = lldb.debugger.GetCommandInterpreter().GetBroadcaster()
    # broadcaster = lldb.debugger.GetSelectedTarget().GetBroadcaster()
    # broadcaster = lldb.debugger.GetSelectedTarget().GetProcess().GetBroadcaster()

    printClassName("SBBroadcaster")
    printFormat("SBBroadcaster", broadcaster)
    printFormat("IsValid", broadcaster.IsValid())
    printFormat("GetName", broadcaster.GetName())


def pSBListener():
    listener = lldb.debugger.GetListener()
    # listener = lldb.debugger.GetSelectedTarget().GetLaunchInfo().GetListener()

    printClassName("SBListener")
    printFormat("SBListener", listener)
    printFormat("IsValid", listener.IsValid())


def pSBLaunchInfo():
    info = lldb.debugger.GetSelectedTarget().GetLaunchInfo()

    printClassName("SBLaunchInfo")
    printFormat("SBLaunchInfo", info)
    printFormat("GetProcessID", info.GetProcessID())
    printFormat("GetUserID", info.GetUserID())
    printFormat("GetGroupID", info.GetGroupID())
    printFormat("UserIDIsValid", info.UserIDIsValid())
    printFormat("GroupIDIsValid", info.GroupIDIsValid())
    printFormat("GetExecutableFile", info.GetExecutableFile())  # SBFileSpec
    printFormat("GetListener", info.GetListener())  # SBListener
    printFormat("GetNumArguments", info.GetNumArguments())
    printFormat("GetNumEnvironmentEntries", info.GetNumEnvironmentEntries())
    printFormat("GetWorkingDirectory", info.GetWorkingDirectory())
    printFormat("GetLaunchFlags", info.GetLaunchFlags())
    printFormat("GetProcessPluginName", info.GetProcessPluginName())
    printFormat("GetShell", info.GetShell())
    printFormat("GetShellExpandArguments", info.GetShellExpandArguments())
    printFormat("GetResumeCount", info.GetResumeCount())
    printFormat("GetLaunchEventData", info.GetLaunchEventData())
    printFormat("GetDetachOnError", info.GetDetachOnError())

    printTraversal(info, "GetNumArguments", "GetArgumentAtIndex")  # [str]
    printTraversal(info, "GetNumEnvironmentEntries", "GetEnvironmentEntryAtIndex")  # [str]


def pSBMemoryRegionInfoList():
    # TODO
    mril = lldb.debugger.GetSelectedTarget().GetProcess().GetMemoryRegions()
