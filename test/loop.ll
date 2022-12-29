; ModuleID = "loop.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"s" = internal global [10 x i32] zeroinitializer
define i32 @"main"()
{
__main:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  store i32 1, i32* %"a"
  %".4" = load i32, i32* %"a"
  br label %".5"
.5:
  %".10" = load i32, i32* %"a"
  %".11" = icmp slt i32 %".10", 10
  %".12" = icmp ne i1 %".11", 0
  br i1 %".12", label %".6", label %".8"
.6:
  %".14" = load i32, i32* %"a"
  %".15" = getelementptr inbounds [10 x i32], [10 x i32]* @"s", i32 0, i32 %".14"
  %".16" = load i32, i32* %"a"
  store i32 %".16", i32* %".15"
  %".18" = load i32, i32* %".15"
  br label %".7"
.7:
  %".20" = load i32, i32* %"a"
  %".21" = add i32 %".20", 1
  store i32 %".21", i32* %"a"
  br label %".5"
.8:
  store i32 1, i32* %"a"
  %".25" = load i32, i32* %"a"
  br label %".26"
.26:
  %".31" = load i32, i32* %"a"
  %".32" = icmp slt i32 %".31", 10
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %".27", label %".29"
.27:
  %".35" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_0", i32 0, i32 0
  %".36" = load i32, i32* %"a"
  %".37" = getelementptr inbounds [10 x i32], [10 x i32]* @"s", i32 0, i32 %".36"
  %".38" = load i32, i32* %".37"
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".35", i32 %".38")
  br label %".28"
.28:
  %".41" = load i32, i32* %"a"
  %".42" = add i32 %".41", 1
  store i32 %".42", i32* %"a"
  br label %".26"
.29:
  %"b" = alloca i32
  store i32 1, i32* %"b"
  store i32 1, i32* %"a"
  %".47" = load i32, i32* %"a"
  br label %".48"
.48:
  %".53" = load i32, i32* %"a"
  %".54" = icmp slt i32 %".53", 10
  %".55" = icmp ne i1 %".54", 0
  br i1 %".55", label %".49", label %".51"
.49:
  store i32 1, i32* %"b"
  %".58" = load i32, i32* %"b"
  br label %".59"
.50:
  %".78" = load i32, i32* %"a"
  %".79" = add i32 %".78", 1
  store i32 %".79", i32* %"a"
  br label %".48"
.51:
  store i32 1, i32* %"b"
  %".83" = load i32, i32* %"b"
  br label %".84"
.59:
  %".64" = load i32, i32* %"b"
  %".65" = icmp slt i32 %".64", 10
  %".66" = icmp ne i1 %".65", 0
  br i1 %".66", label %".60", label %".62"
.60:
  %".68" = getelementptr inbounds [21 x i8], [21 x i8]* @"__string_1", i32 0, i32 0
  %".69" = load i32, i32* %"a"
  %".70" = load i32, i32* %"b"
  %".71" = call i32 (i8*, ...) @"printf"(i8* %".68", i32 %".69", i32 %".70")
  br label %".61"
.61:
  %".73" = load i32, i32* %"b"
  %".74" = add i32 %".73", 1
  store i32 %".74", i32* %"b"
  br label %".59"
.62:
  br label %".50"
.84:
  %".88" = load i32, i32* %"b"
  %".89" = icmp slt i32 %".88", 20
  %".90" = icmp ne i1 %".89", 0
  br i1 %".90", label %".85", label %".86"
.85:
  %".92" = load i32, i32* %"b"
  %".93" = add i32 %".92", 1
  store i32 %".93", i32* %"b"
  %".95" = load i32, i32* %"b"
  %".96" = getelementptr inbounds [7 x i8], [7 x i8]* @"__string_2", i32 0, i32 0
  %".97" = load i32, i32* %"b"
  %".98" = call i32 (i8*, ...) @"printf"(i8* %".96", i32 %".97")
  br label %".84"
.86:
  %".100" = getelementptr inbounds [2 x i8], [2 x i8]* @"__string_3", i32 0, i32 0
  %".101" = call i32 (i8*, ...) @"printf"(i8* %".100")
  ret i32 0
}

@"__string_0" = internal global [4 x i8] c"%d\0a\00"
@"__string_1" = internal global [21 x i8] c"Hello, world! %d %d\0a\00"
@"__string_2" = internal global [7 x i8] c"b: %d \00"
@"__string_3" = internal global [2 x i8] c"\0a\00"