; ModuleID = "global_var.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

@"a" = internal global i32 0
define i32 @"main"() 
{
__main:
  store i32 1, i32* @"a"
  %".3" = load i32, i32* @"a"
  %".4" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_0", i32 0, i32 0
  %".5" = load i32, i32* @"a"
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".5")
  %".7" = load i32, i32* @"a"
  %".8" = mul i32 %".7", 4
  %".9" = add i32 %".8", 1
  store i32 %".9", i32* @"a"
  %".11" = load i32, i32* @"a"
  %".12" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".13" = load i32, i32* @"a"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".13")
  ret i32 0
}

@"__string_0" = internal global [4 x i8] c"%d\0a\00"
@"__string_1" = internal global [4 x i8] c"%d\0a\00"