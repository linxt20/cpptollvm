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
  %".25" = load i32, i32* %".24"
  %".26" = call i32 (i8*, ...) @"scanf"(i8* %".22", i32 %".25")
  br label %".14"
.14:
  %".28" = load i32, i32* %"i"
  %".29" = add i32 %".28", 1
  store i32 %".29", i32* %"i"
  br label %".12"
.15:
  store i32 0, i32* %"i"
  %".33" = load i32, i32* %"i"
  br label %".34"
.34:
  %".39" = load i32, i32* %"i"
  %".40" = load i32, i32* %"n"
  %".41" = sub i32 %".40", 1
  %".42" = icmp slt i32 %".39", %".41"
  %".43" = icmp ne i1 %".42", 0
  br i1 %".43", label %".35", label %".37"
.35:
  %".45" = load i32, i32* %"i"
  %".46" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".45"
  %".47" = load i32, i32* %".46"
  store i32 %".47", i32* %"min"
  %".49" = load i32, i32* %"min"
  %".50" = load i32, i32* %"i"
  store i32 %".50", i32* %"index"
  %".52" = load i32, i32* %"index"
  %".53" = load i32, i32* %"i"
  %".54" = add i32 %".53", 1
  store i32 %".54", i32* %"j"
  %".56" = load i32, i32* %"j"
  br label %".57"
.36:
  %".108" = load i32, i32* %"i"
  %".109" = add i32 %".108", 1
  store i32 %".109", i32* %"i"
  br label %".34"
.37:
  store i32 0, i32* %"i"
  %".113" = load i32, i32* %"i"
  br label %".114"
.57:
  %".62" = load i32, i32* %"j"
  %".63" = load i32, i32* %"n"
  %".64" = icmp slt i32 %".62", %".63"
  %".65" = icmp ne i1 %".64", 0
  br i1 %".65", label %".58", label %".60"
.58:
  %".69" = load i32, i32* %"min"
  %".70" = load i32, i32* %"j"
  %".71" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".70"
  %".72" = load i32, i32* %".71"
  %".73" = icmp sgt i32 %".69", %".72"
  %".74" = icmp ne i1 %".73", 0
  br i1 %".74", label %".67", label %".68"
.59:
  %".86" = load i32, i32* %"j"
  %".87" = add i32 %".86", 1
  store i32 %".87", i32* %"j"
  br label %".57"
.60:
  %".90" = load i32, i32* %"index"
  %".91" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".90"
  %".92" = load i32, i32* %".91"
  store i32 %".92", i32* %"temp"
  %".94" = load i32, i32* %"temp"
  %".95" = load i32, i32* %"index"
  %".96" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".95"
  %".97" = load i32, i32* %"i"
  %".98" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".97"
  %".99" = load i32, i32* %".98"
  store i32 %".99", i32* %".96"
  %".101" = load i32, i32* %".96"
  %".102" = load i32, i32* %"i"
  %".103" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".102"
  %".104" = load i32, i32* %"temp"
  store i32 %".104", i32* %".103"
  %".106" = load i32, i32* %".103"
  br label %".36"
.67:
  %".76" = load i32, i32* %"j"
  %".77" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".76"
  %".78" = load i32, i32* %".77"
  store i32 %".78", i32* %"min"
  %".80" = load i32, i32* %"min"
  %".81" = load i32, i32* %"j"
  store i32 %".81", i32* %"index"
  %".83" = load i32, i32* %"index"
  br label %".68"
.68:
  br label %".59"
.114:
  %".119" = load i32, i32* %"i"
  %".120" = load i32, i32* %"n"
  %".121" = icmp slt i32 %".119", %".120"
  %".122" = icmp ne i1 %".121", 0
  br i1 %".122", label %".115", label %".117"
.115:
  %".124" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".125" = load i32, i32* %"i"
  %".126" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".125"
  %".127" = load i32, i32* %".126"
  %".128" = call i32 (i8*, ...) @"printf"(i8* %".124", i32 %".127")
  br label %".116"
.116:
  %".130" = load i32, i32* %"i"
  %".131" = add i32 %".130", 1
  store i32 %".131", i32* %"i"
  br label %".114"
.117:
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [3 x i8] c"%d\00"
@"__string_2" = internal global [3 x i8] c"%d\00"