; ModuleID = "str.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

@"__string_0" = internal global [14 x i8] c"hello, world!\00"
define i32 @"main"() 
{
__main:
  %".2" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 1
  %".3" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 0
  %".4" = load i8, i8* %".3"
  store i8 %".4", i8* %".2"
  %".6" = load i8, i8* %".2"
  ret i32 0
}
