; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

@"__string_0" = internal global [14 x i8] c"hello, world!\00"
define i32 @"main"() 
{
__main:
  ret void
  %".3" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 1
  %".4" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 0
  %".5" = load i8, i8* %".4"
  store i8 %".5", i8* %".3"
  %".7" = load i8, i8* %".3"
}
