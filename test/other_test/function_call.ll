; ModuleID = "function_call.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define void @"test"() 
{
__test:
  %".2" = getelementptr inbounds [42 x i8], [42 x i8]* @"__string_0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  ret void
}

@"__string_0" = internal global [42 x i8] c"function test being called successfully!\0a\00"
define i32 @"main"() 
{
__main:
  call void @"test"()
  ret i32 0
}
