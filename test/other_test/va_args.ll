; ModuleID = "va_args.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"test"(...) 

define i32 @"main"() 
{
__main:
  %".2" = call i32 (...) @"test"(i32 1, i32 2, i32 3)
  ret i32 0
}
