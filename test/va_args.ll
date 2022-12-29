; ModuleID = "va_args.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"print"(i32 %".1", ...)

define i32 @"main"()
{
__main:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".3" = load i32, i32* %"a"
  %".4" = add i32 %".3", 1
  store i32 %".4", i32* %"a"
  %".6" = load i32, i32* %"a"
  %".7" = load i32, i32* %"a"
  %".8" = call i32 (i32, ...) @"print"(i32 %".7", i32 1, i32 2, i32 3, i32 4, i32 5)
  store i32 %".8", i32* %"a"
  %".10" = load i32, i32* %"a"
  ret void
}
