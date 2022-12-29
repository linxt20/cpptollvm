; ModuleID = "SelectSort.cpp"
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
  %"n" = alloca i32
  store i32 0, i32* %"n"
  %"min" = alloca i32
  store i32 0, i32* %"min"
  %"index" = alloca i32
  store i32 0, i32* %"index"
  %"temp" = alloca i32
  store i32 0, i32* %"temp"
  %"m" = alloca [100 x i32]
  %".8" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"scanf"(i8* %".8", i32* %"n")
  store i32 0, i32* %"i"
  %".11" = load i32, i32* %"i"
  br label %".12"
.12:
  %".17" = load i32, i32* %"i"
  %".18" = load i32, i32* %"n"
  %".19" = icmp slt i32 %".17", %".18"
  %".20" = icmp ne i1 %".19", 0
  br i1 %".20", label %".13", label %".15"
.13:
  %".22" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_1", i32 0, i32 0
  %".23" = load i32, i32* %"i"
  %".24" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".23"
  %".25" = call i32 (i8*, ...) @"scanf"(i8* %".22", i32* %".24")
  br label %".14"
.14:
  %".27" = load i32, i32* %"i"
  %".28" = add i32 %".27", 1
  store i32 %".28", i32* %"i"
  br label %".12"
.15:
  store i32 0, i32* %"i"
  %".32" = load i32, i32* %"i"
  br label %".33"
.33:
  %".38" = load i32, i32* %"i"
  %".39" = load i32, i32* %"n"
  %".40" = icmp slt i32 %".38", %".39"
  %".41" = icmp ne i1 %".40", 0
  br i1 %".41", label %".34", label %".36"
.34:
  %".43" = load i32, i32* %"i"
  %".44" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".43"
  %".45" = load i32, i32* %".44"
  store i32 %".45", i32* %"min"
  %".47" = load i32, i32* %"min"
  %".48" = load i32, i32* %"i"
  store i32 %".48", i32* %"index"
  %".50" = load i32, i32* %"index"
  %".51" = load i32, i32* %"i"
  %".52" = add i32 %".51", 1
  store i32 %".52", i32* %"j"
  %".54" = load i32, i32* %"j"
  br label %".55"
.35:
  %".106" = load i32, i32* %"i"
  %".107" = add i32 %".106", 1
  store i32 %".107", i32* %"i"
  br label %".33"
.36:
  store i32 0, i32* %"i"
  %".111" = load i32, i32* %"i"
  br label %".112"
.55:
  %".60" = load i32, i32* %"j"
  %".61" = load i32, i32* %"n"
  %".62" = icmp slt i32 %".60", %".61"
  %".63" = icmp ne i1 %".62", 0
  br i1 %".63", label %".56", label %".58"
.56:
  %".67" = load i32, i32* %"min"
  %".68" = load i32, i32* %"j"
  %".69" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".68"
  %".70" = load i32, i32* %".69"
  %".71" = icmp sgt i32 %".67", %".70"
  %".72" = icmp ne i1 %".71", 0
  br i1 %".72", label %".65", label %".66"
.57:
  %".84" = load i32, i32* %"j"
  %".85" = add i32 %".84", 1
  store i32 %".85", i32* %"j"
  br label %".55"
.58:
  %".88" = load i32, i32* %"index"
  %".89" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".88"
  %".90" = load i32, i32* %".89"
  store i32 %".90", i32* %"temp"
  %".92" = load i32, i32* %"temp"
  %".93" = load i32, i32* %"index"
  %".94" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".93"
  %".95" = load i32, i32* %"i"
  %".96" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".95"
  %".97" = load i32, i32* %".96"
  store i32 %".97", i32* %".94"
  %".99" = load i32, i32* %".94"
  %".100" = load i32, i32* %"i"
  %".101" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".100"
  %".102" = load i32, i32* %"temp"
  store i32 %".102", i32* %".101"
  %".104" = load i32, i32* %".101"
  br label %".35"
.65:
  %".74" = load i32, i32* %"j"
  %".75" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".74"
  %".76" = load i32, i32* %".75"
  store i32 %".76", i32* %"min"
  %".78" = load i32, i32* %"min"
  %".79" = load i32, i32* %"j"
  store i32 %".79", i32* %"index"
  %".81" = load i32, i32* %"index"
  br label %".66"
.66:
  br label %".57"
.112:
  %".117" = load i32, i32* %"i"
  %".118" = load i32, i32* %"n"
  %".119" = icmp slt i32 %".117", %".118"
  %".120" = icmp ne i1 %".119", 0
  br i1 %".120", label %".113", label %".115"
.113:
  %".122" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_2", i32 0, i32 0
  %".123" = load i32, i32* %"i"
  %".124" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".123"
  %".125" = load i32, i32* %".124"
  %".126" = call i32 (i8*, ...) @"printf"(i8* %".122", i32 %".125")
  br label %".114"
.114:
  %".128" = load i32, i32* %"i"
  %".129" = add i32 %".128", 1
  store i32 %".129", i32* %"i"
  br label %".112"
.115:
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [3 x i8] c"%d\00"
@"__string_2" = internal global [4 x i8] c"%d \00"