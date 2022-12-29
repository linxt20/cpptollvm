; ModuleID = "branch.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"() 
{
__main:
  %"a" = alloca i32
  %".2" = sub i32 0, 1
  store i32 %".2", i32* %"a"
  %".7" = icmp ne i32 1, 0
  br i1 %".7", label %".4", label %".5"
.4:
  %".9" = sub i32 0, 1
  br label %".6"
.5:
  br label %".6"
.6:
  %"b" = alloca i32
  store i32 1, i32* %"b"
  %".16" = load i32, i32* %"a"
  %".17" = icmp ne i32 %".16", 0
  br i1 %".17", label %".13", label %".14"
.13:
  %".19" = load i32, i32* %"a"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %"a"
  %".22" = load i32, i32* %"a"
  br label %".15"
.14:
  %".24" = load i32, i32* %"a"
  %".25" = sub i32 %".24", 1
  store i32 %".25", i32* %"a"
  %".27" = load i32, i32* %"a"
  br label %".15"
.15:
  ret i32 0
}
