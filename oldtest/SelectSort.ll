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
  %".41" = icmp slt i32 %".39", %".40"
  %".42" = icmp ne i1 %".41", 0
  br i1 %".42", label %".35", label %".37"
.35:
  %".44" = load i32, i32* %"i"
  %".45" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".44"
  %".46" = load i32, i32* %".45"
  store i32 %".46", i32* %"min"
  %".48" = load i32, i32* %"min"
  %".49" = load i32, i32* %"i"
  store i32 %".49", i32* %"index"
  %".51" = load i32, i32* %"index"
  %".52" = load i32, i32* %"i"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"j"
  %".55" = load i32, i32* %"j"
  br label %".56"
.36:
  %".107" = load i32, i32* %"i"
  %".108" = add i32 %".107", 1
  store i32 %".108", i32* %"i"
  br label %".34"
.37:
  store i32 0, i32* %"i"
  %".112" = load i32, i32* %"i"
  br label %".113"
.56:
  %".61" = load i32, i32* %"j"
  %".62" = load i32, i32* %"n"
  %".63" = icmp slt i32 %".61", %".62"
  %".64" = icmp ne i1 %".63", 0
  br i1 %".64", label %".57", label %".59"
.57:
  %".68" = load i32, i32* %"min"
  %".69" = load i32, i32* %"j"
  %".70" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".69"
  %".71" = load i32, i32* %".70"
  %".72" = icmp sgt i32 %".68", %".71"
  %".73" = icmp ne i1 %".72", 0
  br i1 %".73", label %".66", label %".67"
.58:
  %".85" = load i32, i32* %"j"
  %".86" = add i32 %".85", 1
  store i32 %".86", i32* %"j"
  br label %".56"
.59:
  %".89" = load i32, i32* %"index"
  %".90" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".89"
  %".91" = load i32, i32* %".90"
  store i32 %".91", i32* %"temp"
  %".93" = load i32, i32* %"temp"
  %".94" = load i32, i32* %"index"
  %".95" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".94"
  %".96" = load i32, i32* %"i"
  %".97" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".96"
  %".98" = load i32, i32* %".97"
  store i32 %".98", i32* %".95"
  %".100" = load i32, i32* %".95"
  %".101" = load i32, i32* %"i"
  %".102" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".101"
  %".103" = load i32, i32* %"temp"
  store i32 %".103", i32* %".102"
  %".105" = load i32, i32* %".102"
  br label %".36"
.66:
  %".75" = load i32, i32* %"j"
  %".76" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".75"
  %".77" = load i32, i32* %".76"
  store i32 %".77", i32* %"min"
  %".79" = load i32, i32* %"min"
  %".80" = load i32, i32* %"j"
  store i32 %".80", i32* %"index"
  %".82" = load i32, i32* %"index"
  br label %".67"
.67:
  br label %".58"
.113:
  %".118" = load i32, i32* %"i"
  %".119" = load i32, i32* %"n"
  %".120" = icmp slt i32 %".118", %".119"
  %".121" = icmp ne i1 %".120", 0
  br i1 %".121", label %".114", label %".116"
.114:
  %".123" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".124" = load i32, i32* %"i"
  %".125" = getelementptr inbounds [100 x i32], [100 x i32]* %"m", i32 0, i32 %".124"
  %".126" = load i32, i32* %".125"
  %".127" = call i32 (i8*, ...) @"printf"(i8* %".123", i32 %".126")
  br label %".115"
.115:
  %".129" = load i32, i32* %"i"
  %".130" = add i32 %".129", 1
  store i32 %".130", i32* %"i"
  br label %".113"
.116:
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [3 x i8] c"%d\00"
@"__string_2" = internal global [3 x i8] c"%d\00"