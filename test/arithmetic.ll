; ModuleID = "arithmetic.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
__main:
  %"a" = alloca i32
  store i32 2531, i32* %"a"
  %"b" = alloca i32
  store i32 46, i32* %"b"
  %"c" = alloca i32
  %".4" = load i32, i32* %"b"
  %".5" = load i32, i32* %"a"
  %".6" = add i32 %".4", %".5"
  store i32 %".6", i32* %"c"
  %".8" = load i32, i32* %"b"
  %".9" = load i32, i32* %"a"
  %".10" = sub i32 %".8", %".9"
  store i32 %".10", i32* %"c"
  %".12" = load i32, i32* %"c"
  %".13" = load i32, i32* %"c"
  %".14" = load i32, i32* %"b"
  %".15" = mul i32 %".14", 50
  %".16" = add i32 %".13", %".15"
  store i32 %".16", i32* %"c"
  %".18" = load i32, i32* %"c"
  %"d" = alloca i32
  %".19" = load i32, i32* %"c"
  %".20" = load i32, i32* %"b"
  %".21" = mul i32 %".19", %".20"
  store i32 %".21", i32* %"d"
  %".23" = load i32, i32* %"a"
  %".24" = load i32, i32* %"b"
  %".25" = add i32 %".23", %".24"
  store i32 %".25", i32* %"c"
  %".27" = load i32, i32* %"c"
  %"e" = alloca i1
  %".28" = load i32, i32* %"d"
  %".29" = icmp sgt i32 %".28", 10
  store i1 %".29", i1* %"e"
  %".31" = load i1, i1* %"e"
  %".32" = icmp ne i1 %".31", 0
  store i1 %".32", i1* %"e"
  %".34" = load i1, i1* %"e"
  %"f" = alloca i1
  %".35" = load i32, i32* %"d"
  %".36" = icmp slt i32 %".35", 0
  store i1 %".36", i1* %"f"
  %".38" = load i1, i1* %"f"
  %".39" = load i1, i1* %"e"
  %".40" = xor i1 %".38", %".39"
  store i1 %".40", i1* %"f"
  %".42" = load i1, i1* %"f"
  ret i32 0
}
