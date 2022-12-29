; ModuleID = "var.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"() 
{
__main:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  store i32 2, i32* %"a"
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"a"
  %".6" = add i32 %".5", 1
  store i32 %".6", i32* %"a"
  %".8" = load i32, i32* %"a"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  %".10" = load i32, i32* %"b"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* %"b"
  %".13" = load i32, i32* %"b"
  %".14" = load i32, i32* %"a"
  %".15" = load i32, i32* %"b"
  %".16" = add i32 %".14", %".15"
  store i32 %".16", i32* %"b"
  %".18" = load i32, i32* %"b"
  %".19" = load i32, i32* %"a"
  %".20" = sub i32 0, %".19"
  store i32 %".20", i32* %"a"
  %".22" = load i32, i32* %"a"
  %"c" = alloca double
  store double 0x3ff0000000000000, double* %"c"
  %".24" = load double, double* %"c"
  %".25" = sitofp i32 1 to double
  %".26" = fadd double %".24", %".25"
  store double %".26", double* %"c"
  %".28" = load double, double* %"c"
  ret i32 0
}
