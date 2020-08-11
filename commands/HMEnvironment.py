# The MIT License (MIT)
#
# Copyright (c) 2020 Huimao Chen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import lldb
import HMLLDBHelpers as HM


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f HMEnvironment.environment environment -h "Show diagnostic environment."')


def environment(debugger, command, exe_ctx, result, internal_dict):
    """
    Syntax:
        environment

    Examples:
        (lldb) environment

    This command is implemented in HMEnvironment.py
    """


    # 1.LLDB version
    # 2.Target triple
    # 3.Optimized
    # 4.Xcode version
    # 5.Xcode build version
    # 6.Model identifier
    # 7.System version

    HM.DPrint('[LLDB version] ' + debugger.GetVersionString())

    HM.DPrint('[Target triple] ' + debugger.GetSelectedTarget().GetTriple())

    optimizedFalseCount = 0
    optimizedTrueCount = 0
    symbolContextList = lldb.debugger.GetSelectedTarget().FindFunctions("viewDidLoad")
    for i in range(symbolContextList.GetSize()):
        if i == 1000:
            break
        ctx = symbolContextList.GetContextAtIndex(i)
        if ctx.GetFunction().IsValid():
            if ctx.GetFunction().GetIsOptimized():
                optimizedTrueCount += 1
            else:
                optimizedFalseCount += 1

    HM.DPrint('[Optimized] ' + f'False: {optimizedFalseCount}  True: {optimizedTrueCount}')

    XcodeVersionValue = HM.evaluateExpressionValue('(NSString *)([NSBundle mainBundle].infoDictionary[@"DTXcode"] ?: @"-")')
    HM.DPrint('[Xcode version] ' + XcodeVersionValue.GetObjectDescription())

    XcodeBuildVersionValue = HM.evaluateExpressionValue('(NSString *)([NSBundle mainBundle].infoDictionary[@"DTXcodeBuild"] ?: @"-")')
    HM.DPrint('[Xcode build version] ' + XcodeBuildVersionValue.GetObjectDescription())

    command_script = '''
        struct utsname systemInfo;
        (int)uname(&systemInfo);
        NSString *modelIdentifier = [NSString stringWithCString:systemInfo.machine encoding:(NSStringEncoding)4];
        modelIdentifier;
    '''
    modelIDValue = HM.evaluateExpressionValue(command_script)
    HM.DPrint('[Model identifier] ' + modelIDValue.GetObjectDescription())

    SystemVersionValue = HM.evaluateExpressionValue('(NSString *)[[NSString alloc] initWithFormat:@"%@ %@", [[UIDevice currentDevice] systemName], [[UIDevice currentDevice] systemVersion]]')
    HM.DPrint('[System version] ' + SystemVersionValue.GetObjectDescription())
