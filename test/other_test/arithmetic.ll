; ModuleID = "arithmetic.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

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
  %".8" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_0", i32 0, i32 0
  %".9" = load i32, i32* %"c"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".9")
  %".11" = load i32, i32* %"b"
  %".12" = load i32, i32* %"a"
  %".13" = sub i32 %".11", %".12"
  store i32 %".13", i32* %"c"
  %".15" = load i32, i32* %"c"
  %".16" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".17" = load i32, i32* %"c"
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".16", i32 %".17")
  %".19" = load i32, i32* %"c"
  %".20" = load i32, i32* %"b"
  %".21" = mul i32 %".20", 50
  %".22" = add i32 %".19", %".21"
  store i32 %".22", i32* %"c"
  %".24" = load i32, i32* %"c"
  %".25" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_2", i32 0, i32 0
  %".26" = load i32, i32* %"c"
  %".27" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %".26")
  %"d" = alloca double
  store double 0x3ff3ae147ae147ae, double* %"d"
  %".29" = getelementptr inbounds [5 x i8], [5 x i8]* @"__string_3", i32 0, i32 0
  %".30" = load double, double* %"d"
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".29", double %".30")
  %".32" = load i32, i32* %"a"
  %".33" = load i32, i32* %"b"
  %".34" = sdiv i32 %".32", %".33"
  store i32 %".34", i32* %"c"
  %".36" = load i32, i32* %"c"
  %".37" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_4", i32 0, i32 0
  %".38" = load i32, i32* %"c"
  %".39" = call i32 (i8*, ...) @"printf"(i8* %".37", i32 %".38")
  %"e" = alloca i1
  %".40" = load double, double* %"d"
  %".41" = sitofp i32 10 to double
  %".42" = fcmp ogt double %".40", %".41"
  store i1 %".42", i1* %"e"
  %".44" = load i1, i1* %"e"
  %".45" = icmp ne i1 %".44", 0
  store i1 %".45", i1* %"e"
  %".47" = load i1, i1* %"e"
  %"f" = alloca i1
  %".48" = load double, double* %"d"
  %".49" = sitofp i32 0 to double
  %".50" = fcmp olt double %".48", %".49"
  store i1 %".50", i1* %"f"
  %".52" = load i1, i1* %"f"
  %".53" = load i1, i1* %"e"
  %".54" = xor i1 %".52", %".53"
  store i1 %".54", i1* %"f"
  %".56" = load i1, i1* %"f"
  ret i32 0
}

@"__string_0" = internal global [4 x i8] c"%d\0a\00"
@"__string_1" = internal global [4 x i8] c"%d\0a\00"
@"__string_2" = internal global [4 x i8] c"%d\0a\00"
@"__string_3" = internal global [5 x i8] c"%lf\0a\00"
@"__string_4" = internal global [4 x i8] c"%d\0a\00"