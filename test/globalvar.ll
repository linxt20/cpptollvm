; ModuleID = "globalvar.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

@"a" = internal global i32 0
define i32 @"main"() 
{
__main:
  store i32 1, i32* @"a"
  %".3" = load i32, i32* @"a"
  %".4" = load i32, i32* @"a"
  %".5" = add i32 %".4", 1
  store i32 %".5", i32* @"a"
  %".7" = load i32, i32* @"a"
  %".8" = add i32 %".7", 1
  store i32 %".8", i32* @"a"
  %".10" = load i32, i32* @"a"
  ret i32 0
}
