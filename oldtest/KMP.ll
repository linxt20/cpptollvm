; ModuleID = "KMP.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"stringone" = internal global [100 x i8] zeroinitializer
@"stringanother" = internal global [100 x i8] zeroinitializer
@"nextone" = internal global [100 x i32] zeroinitializer
@"len" = internal global i32 0
define i32 @"KMP"()
{
__KMP:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  %"flag" = alloca i32
  store i32 0, i32* %"flag"
  %"pos" = alloca i32
  store i32 0, i32* %"pos"
  br label %".6"
.6:
  %".10" = load i32, i32* %"i"
  %".11" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".10"
  %".12" = load i8, i8* %".11"
  %".13" = sext i8 %".12" to i32
  %".14" = icmp ne i32 %".13", 0
  %".15" = icmp ne i1 %".14", 0
  br i1 %".15", label %".7", label %".8"
.7:
  %".20" = load i32, i32* %"j"
  %".21" = sub i32 0, 1
  %".22" = icmp eq i32 %".20", %".21"
  %".23" = load i32, i32* %"i"
  %".24" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".23"
  %".25" = load i8, i8* %".24"
  %".26" = load i32, i32* %"j"
  %".27" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 %".26"
  %".28" = load i8, i8* %".27"
  %".29" = icmp eq i8 %".25", %".28"
  %".30" = icmp ne i1 %".22", 0
  %".31" = icmp ne i1 %".29", 0
  %".32" = or i1 %".30", %".31"
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %".17", label %".18"
.8:
  %".73" = load i32, i32* %"flag"
  %".74" = icmp eq i32 %".73", 0
  %".75" = icmp ne i1 %".74", 0
  br i1 %".75", label %".71", label %".72"
.17:
  %".35" = load i32, i32* %"i"
  %".36" = add i32 %".35", 1
  store i32 %".36", i32* %"i"
  %".38" = load i32, i32* %"i"
  %".39" = load i32, i32* %"j"
  %".40" = add i32 %".39", 1
  store i32 %".40", i32* %"j"
  %".42" = load i32, i32* %"j"
  %".45" = load i32, i32* %"j"
  %".46" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 %".45"
  %".47" = load i8, i8* %".46"
  %".48" = sext i8 %".47" to i32
  %".49" = icmp eq i32 %".48", 0
  %".50" = icmp ne i1 %".49", 0
  br i1 %".50", label %".43", label %".44"
.18:
  %".64" = load i32, i32* %"j"
  %".65" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 %".64"
  %".66" = load i32, i32* %".65"
  store i32 %".66", i32* %"j"
  %".68" = load i32, i32* %"j"
  br label %".19"
.19:
  br label %".6"
.43:
  %".52" = load i32, i32* %"i"
  %".53" = load i32, i32* @"len"
  %".54" = sub i32 %".52", %".53"
  store i32 %".54", i32* %"pos"
  %".56" = load i32, i32* %"pos"
  %".57" = getelementptr inbounds [11 x i8], [11 x i8]* @"__string_0", i32 0, i32 0
  %".58" = load i32, i32* %"pos"
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".57", i32 %".58")
  store i32 1, i32* %"flag"
  %".61" = load i32, i32* %"flag"
  br label %".44"
.44:
  br label %".19"
.71:
  %".77" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_1", i32 0, i32 0
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".77")
  br label %".72"
.72:
  ret void
}

@"__string_0" = internal global [11 x i8] c"place: %d\0a\00"
@"__string_1" = internal global [6 x i8] c"false\00"
define i32 @"main"()
{
__main:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"k" = alloca i32
  store i32 0, i32* %"k"
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".5" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".4", i8* %".5")
  %".7" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_3", i32 0, i32 0
  %".8" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"scanf"(i8* %".7", i8* %".8")
  store i32 0, i32* @"len"
  %".11" = load i32, i32* @"len"
  br label %".12"
.12:
  %".16" = load i32, i32* @"len"
  %".17" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 %".16"
  %".18" = load i8, i8* %".17"
  %".19" = sext i8 %".18" to i32
  %".20" = icmp ne i32 %".19", 0
  %".21" = icmp ne i1 %".20", 0
  br i1 %".21", label %".13", label %".14"
.13:
  %".23" = load i32, i32* @"len"
  %".24" = add i32 %".23", 1
  store i32 %".24", i32* @"len"
  %".26" = load i32, i32* @"len"
  br label %".12"
.14:
  %".28" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 0
  %".29" = sub i32 0, 1
  store i32 %".29", i32* %".28"
  %".31" = load i32, i32* %".28"
  store i32 1, i32* %"i"
  %".33" = load i32, i32* %"i"
  br label %".34"
.34:
  %".39" = load i32, i32* %"i"
  %".40" = load i32, i32* @"len"
  %".41" = icmp slt i32 %".39", %".40"
  %".42" = icmp ne i1 %".41", 0
  br i1 %".42", label %".35", label %".37"
.35:
  %".44" = load i32, i32* %"i"
  %".45" = sub i32 %".44", 1
  %".46" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 %".45"
  %".47" = load i32, i32* %".46"
  store i32 %".47", i32* %"k"
  %".49" = load i32, i32* %"k"
  %".50" = load i32, i32* %"i"
  %".51" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 %".50"
  store i32 0, i32* %".51"
  %".53" = load i32, i32* %".51"
  br label %".54"
.36:
  %".90" = load i32, i32* %"i"
  %".91" = add i32 %".90", 1
  store i32 %".91", i32* %"i"
  %".93" = load i32, i32* %"i"
  br label %".34"
.37:
  %".95" = call i32 @"KMP"()
  ret i32 0
.54:
  %".58" = load i32, i32* %"k"
  %".59" = icmp sge i32 %".58", 0
  %".60" = icmp ne i1 %".59", 0
  br i1 %".60", label %".55", label %".56"
.55:
  %".65" = load i32, i32* %"i"
  %".66" = sub i32 %".65", 1
  %".67" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 %".66"
  %".68" = load i8, i8* %".67"
  %".69" = load i32, i32* %"k"
  %".70" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringanother", i32 0, i32 %".69"
  %".71" = load i8, i8* %".70"
  %".72" = icmp eq i8 %".68", %".71"
  %".73" = icmp ne i1 %".72", 0
  br i1 %".73", label %".62", label %".63"
.56:
  br label %".36"
.62:
  %".75" = load i32, i32* %"i"
  %".76" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 %".75"
  %".77" = load i32, i32* %"k"
  %".78" = add i32 %".77", 1
  store i32 %".78", i32* %".76"
  %".80" = load i32, i32* %".76"
  br label %".56"
.63:
  %".82" = load i32, i32* %"k"
  %".83" = getelementptr inbounds [100 x i32], [100 x i32]* @"nextone", i32 0, i32 %".82"
  %".84" = load i32, i32* %".83"
  store i32 %".84", i32* %"k"
  %".86" = load i32, i32* %"k"
  br label %".64"
.64:
  br label %".54"
}

@"__string_2" = internal global [3 x i8] c"%s\00"
@"__string_3" = internal global [3 x i8] c"%s\00"