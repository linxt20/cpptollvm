; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

define i32 @"f"(i32 %".1")
{
__f:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 1, i32* %"b"
  %".5" = load i32, i32* %"a"
  %".6" = load i32, i32* %"b"
  %".7" = add i32 %".5", %".6"
  store i32 %".7", i32* %"a"
  %".9" = load i32, i32* %"a"
  %".10" = load i32, i32* %"b"
  %".11" = load i32, i32* %"a"
  %".12" = mul i32 %".10", %".11"
  store i32 %".12", i32* %"b"
  %".14" = load i32, i32* %"b"
  %".15" = load i32, i32* %"a"
  %".16" = add i32 %".15", 1
  ret i32 %".16"
}

define i32 @"g"(i32 %".1", double %".2")
{
__g:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca double
  store double %".2", double* %"b"
  %".6" = load i32, i32* %"a"
  ret i32 %".6"
}

define i32 @"main"()
{
__main:
  %"d" = alloca i32
  store i32 1, i32* %"d"
  %".3" = load i32, i32* %"d"
  %".4" = call i32 @"f"(i32 %".3")
  %"b" = alloca double
  store double              0x0, double* %"b"
  %".6" = load i32, i32* %"d"
  %".7" = load double, double* %"b"
  %".8" = call i32 @"g"(i32 %".6", double %".7")
  ret i32 0
}
