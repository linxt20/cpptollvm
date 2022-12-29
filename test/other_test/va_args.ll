; ModuleID = "va_args.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i32 %".1", ...) 

define i32 @"main"() 
{
__main:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".3" = load i32, i32* %"a"
  %".4" = call i32 (i32, ...) @"printf"(i32 %".3", i32 1, i32 2, i32 3)
  ret void
}
