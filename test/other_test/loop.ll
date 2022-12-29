; ModuleID = "loop.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

@"s" = internal global [10 x i32] zeroinitializer
define i32 @"main"() 
{
__main:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  store i32 1, i32* %"i"
  %".5" = load i32, i32* %"i"
  br label %".6"
.6:
  %".11" = load i32, i32* %"i"
  %".12" = icmp slt i32 %".11", 10
  %".13" = icmp ne i1 %".12", 0
  br i1 %".13", label %".7", label %".9"
.7:
  store i32 1, i32* %"j"
  %".16" = load i32, i32* %"j"
  br label %".17"
.8:
  %".36" = load i32, i32* %"i"
  %".37" = add i32 %".36", 1
  store i32 %".37", i32* %"i"
  br label %".6"
.9:
  store i32 0, i32* %"i"
  %".41" = load i32, i32* %"i"
  br label %".42"
.17:
  %".22" = load i32, i32* %"j"
  %".23" = icmp slt i32 %".22", 10
  %".24" = icmp ne i1 %".23", 0
  br i1 %".24", label %".18", label %".20"
.18:
  %".26" = getelementptr inbounds [21 x i8], [21 x i8]* @"__string_0", i32 0, i32 0
  %".27" = load i32, i32* %"i"
  %".28" = load i32, i32* %"j"
  %".29" = call i32 (i8*, ...) @"printf"(i8* %".26", i32 %".27", i32 %".28")
  br label %".19"
.19:
  %".31" = load i32, i32* %"j"
  %".32" = add i32 %".31", 1
  store i32 %".32", i32* %"j"
  br label %".17"
.20:
  br label %".8"
.42:
  %".46" = load i32, i32* %"i"
  %".47" = icmp slt i32 %".46", 10
  %".48" = icmp ne i1 %".47", 0
  br i1 %".48", label %".43", label %".44"
.43:
  %".50" = load i32, i32* %"i"
  %".51" = add i32 %".50", 1
  store i32 %".51", i32* %"i"
  %".53" = load i32, i32* %"i"
  %".54" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".55" = load i32, i32* %"i"
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".54", i32 %".55")
  br label %".42"
.44:
  ret i32 0
}

@"__string_0" = internal global [21 x i8] c"Hello, world! %d %d\0a\00"
@"__string_1" = internal global [4 x i8] c"%d \00"