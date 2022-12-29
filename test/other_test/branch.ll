; ModuleID = "branch.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
__main:
  %"a" = alloca i32
  %".2" = sub i32 0, 1
  store i32 %".2", i32* %"a"
  %".7" = icmp ne i32 1, 0
  br i1 %".7", label %".4", label %".5"
.4:
  %".9" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  br label %".6"
.5:
  %".12" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_1", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  br label %".6"
.6:
  %"b" = alloca i32
  store i32 1, i32* %"b"
  %".19" = load i32, i32* %"a"
  %".20" = icmp ne i32 %".19", 0
  br i1 %".20", label %".16", label %".17"
.16:
  %".22" = load i32, i32* %"a"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"a"
  %".25" = load i32, i32* %"a"
  %".26" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_2", i32 0, i32 0
  %".27" = load i32, i32* %"a"
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".27")
  br label %".18"
.17:
  %".30" = load i32, i32* %"a"
  %".31" = sub i32 %".30", 1
  store i32 %".31", i32* %"a"
  %".33" = load i32, i32* %"a"
  %".34" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_3", i32 0, i32 0
  %".35" = load i32, i32* %"a"
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".34", i32 %".35")
  br label %".18"
.18:
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"1\0a\00"
@"__string_1" = internal global [3 x i8] c"0\0a\00"
@"__string_2" = internal global [4 x i8] c"%d\0a\00"
@"__string_3" = internal global [4 x i8] c"%d\0a\00"