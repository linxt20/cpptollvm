; ModuleID = "palindrome.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
__main:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  %"m" = alloca [100 x i8]
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", [100 x i8]* %"m")
  br label %".6"
.6:
  %".10" = load i32, i32* %"i"
  %".11" = getelementptr inbounds [100 x i8], [100 x i8]* %"m", i32 0, i32 %".10"
  %".12" = load i8, i8* %".11"
  %".13" = icmp ne i8 %".12", 0
  br i1 %".13", label %".7", label %".8"
.7:
  %".15" = load i32, i32* %"i"
  %".16" = add i32 %".15", 1
  store i32 %".16", i32* %"i"
  br label %".6"
.8:
  %".19" = load i32, i32* %"i"
  %".20" = sub i32 %".19", 1
  store i32 %".20", i32* %"i"
  br label %".22"
.22:
  %".26" = load i32, i32* %"j"
  %".27" = load i32, i32* %"i"
  %".28" = icmp slt i32 %".26", %".27"
  %".29" = icmp ne i1 %".28", 0
  br i1 %".29", label %".23", label %".24"
.23:
  %".33" = load i32, i32* %"j"
  %".34" = getelementptr inbounds [100 x i8], [100 x i8]* %"m", i32 0, i32 %".33"
  %".35" = load i8, i8* %".34"
  %".36" = load i32, i32* %"i"
  %".37" = getelementptr inbounds [100 x i8], [100 x i8]* %"m", i32 0, i32 %".36"
  %".38" = load i8, i8* %".37"
  %".39" = icmp ne i8 %".35", %".38"
  %".40" = icmp ne i1 %".39", 0
  br i1 %".40", label %".31", label %".32"
.24:
  %".52" = getelementptr inbounds [5 x i8], [5 x i8]* @"__string_2", i32 0, i32 0
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52")
  ret i32 0
.31:
  %".42" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_1", i32 0, i32 0
  %".43" = call i32 (i8*, ...) @"printf"(i8* %".42")
  ret i32 0
.32:
  %".45" = load i32, i32* %"i"
  %".46" = sub i32 %".45", 1
  store i32 %".46", i32* %"i"
  %".48" = load i32, i32* %"j"
  %".49" = add i32 %".48", 1
  store i32 %".49", i32* %"j"
  br label %".22"
}

@"__string_0" = internal global [3 x i8] c"%s\00"
@"__string_1" = internal global [6 x i8] c"False\00"
@"__string_2" = internal global [5 x i8] c"True\00"