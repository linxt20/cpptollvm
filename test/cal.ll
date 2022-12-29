; ModuleID = "cal.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"final" = internal global [100 x i8] zeroinitializer
@"strs" = internal global [100 x i8] zeroinitializer
@"stringone" = internal global [100 x i8] zeroinitializer
@"judgezero" = internal global i32 0
define i32 @"Polish"()
{
__Polish:
  %"s1" = alloca [100 x i8]
  %"index_1" = alloca i32
  store i32 0, i32* %"index_1"
  %"len" = alloca i32
  store i32 0, i32* %"len"
  store i32 0, i32* %"len"
  %".5" = load i32, i32* %"len"
  br label %".6"
.6:
  %".11" = load i32, i32* %"len"
  %".12" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".11"
  %".13" = load i8, i8* %".12"
  %".14" = sext i8 %".13" to i32
  %".15" = icmp ne i32 %".14", 0
  %".16" = icmp ne i1 %".15", 0
  br i1 %".16", label %".7", label %".9"
.7:
  br label %".8"
.8:
  %".19" = load i32, i32* %"len"
  %".20" = add i32 %".19", 1
  store i32 %".20", i32* %"len"
  %".22" = load i32, i32* %"len"
  br label %".6"
.9:
  %".24" = getelementptr inbounds [22 x i8], [22 x i8]* @"__string_0", i32 0, i32 0
  %".25" = load i32, i32* %"len"
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".25")
  %"t" = alloca i32
  store i32 1, i32* %"t"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %".29"
.29:
  %".33" = load i32, i32* %"i"
  %".34" = load i32, i32* %"len"
  %".35" = icmp slt i32 %".33", %".34"
  %".36" = icmp ne i1 %".35", 0
  br i1 %".36", label %".30", label %".31"
.30:
  %".41" = load i32, i32* %"i"
  %".42" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".41"
  %".43" = load i8, i8* %".42"
  %".44" = sext i8 %".43" to i32
  %".45" = icmp eq i32 %".44", 91
  %".46" = icmp ne i1 %".45", 0
  br i1 %".46", label %".38", label %".39"
.31:
  br label %".292"
.38:
  %".48" = load i32, i32* %"index_1"
  %".49" = add i32 %".48", 1
  store i32 %".49", i32* %"index_1"
  %".51" = load i32, i32* %"index_1"
  %".52" = load i32, i32* %"index_1"
  %".53" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".52"
  %".54" = trunc i32 91 to i8
  store i8 %".54", i8* %".53"
  %".56" = load i8, i8* %".53"
  %".57" = load i32, i32* %"i"
  %".58" = add i32 %".57", 1
  store i32 %".58", i32* %"i"
  %".60" = load i32, i32* %"i"
  br label %".40"
.39:
  %".65" = load i32, i32* %"i"
  %".66" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".65"
  %".67" = load i8, i8* %".66"
  %".68" = sext i8 %".67" to i32
  %".69" = icmp eq i32 %".68", 93
  %".70" = icmp ne i1 %".69", 0
  br i1 %".70", label %".62", label %".63"
.40:
  br label %".29"
.62:
  br label %".72"
.63:
  %".111" = load i32, i32* %"i"
  %".112" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".111"
  %".113" = load i8, i8* %".112"
  %".114" = sext i8 %".113" to i32
  %".115" = icmp eq i32 %".114", 43
  %".116" = load i32, i32* %"i"
  %".117" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".116"
  %".118" = load i8, i8* %".117"
  %".119" = sext i8 %".118" to i32
  %".120" = icmp eq i32 %".119", 45
  %".121" = icmp ne i1 %".115", 0
  %".122" = icmp ne i1 %".120", 0
  %".123" = or i1 %".121", %".122"
  %".124" = icmp ne i1 %".123", 0
  br i1 %".124", label %".108", label %".109"
.64:
  br label %".40"
.72:
  %".76" = load i32, i32* %"index_1"
  %".77" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".76"
  %".78" = load i8, i8* %".77"
  %".79" = sext i8 %".78" to i32
  %".80" = icmp ne i32 %".79", 91
  %".81" = icmp ne i1 %".80", 0
  br i1 %".81", label %".73", label %".74"
.73:
  %".83" = load i32, i32* %"t"
  %".84" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".83"
  %".85" = load i32, i32* %"index_1"
  %".86" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".85"
  %".87" = load i8, i8* %".86"
  store i8 %".87", i8* %".84"
  %".89" = load i8, i8* %".84"
  %".90" = load i32, i32* %"t"
  %".91" = add i32 %".90", 1
  store i32 %".91", i32* %"t"
  %".93" = load i32, i32* %"t"
  %".94" = load i32, i32* %"index_1"
  %".95" = sub i32 %".94", 1
  store i32 %".95", i32* %"index_1"
  %".97" = load i32, i32* %"index_1"
  br label %".72"
.74:
  %".99" = load i32, i32* %"index_1"
  %".100" = sub i32 %".99", 1
  store i32 %".100", i32* %"index_1"
  %".102" = load i32, i32* %"index_1"
  %".103" = load i32, i32* %"i"
  %".104" = add i32 %".103", 1
  store i32 %".104", i32* %"i"
  %".106" = load i32, i32* %"i"
  br label %".64"
.108:
  br label %".126"
.109:
  %".177" = load i32, i32* %"i"
  %".178" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".177"
  %".179" = load i8, i8* %".178"
  %".180" = sext i8 %".179" to i32
  %".181" = icmp eq i32 %".180", 42
  %".182" = load i32, i32* %"i"
  %".183" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".182"
  %".184" = load i8, i8* %".183"
  %".185" = sext i8 %".184" to i32
  %".186" = icmp eq i32 %".185", 47
  %".187" = icmp ne i1 %".181", 0
  %".188" = icmp ne i1 %".186", 0
  %".189" = or i1 %".187", %".188"
  %".190" = icmp ne i1 %".189", 0
  br i1 %".190", label %".174", label %".175"
.110:
  br label %".64"
.126:
  %".130" = load i32, i32* %"index_1"
  %".131" = icmp ne i32 %".130", 0
  %".132" = load i32, i32* %"index_1"
  %".133" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".132"
  %".134" = load i8, i8* %".133"
  %".135" = sext i8 %".134" to i32
  %".136" = icmp ne i32 %".135", 91
  %".137" = icmp ne i1 %".131", 0
  %".138" = icmp ne i1 %".136", 0
  %".139" = and i1 %".137", %".138"
  %".140" = icmp ne i1 %".139", 0
  br i1 %".140", label %".127", label %".128"
.127:
  %".142" = load i32, i32* %"t"
  %".143" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".142"
  %".144" = load i32, i32* %"index_1"
  %".145" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".144"
  %".146" = load i8, i8* %".145"
  store i8 %".146", i8* %".143"
  %".148" = load i8, i8* %".143"
  %".149" = load i32, i32* %"t"
  %".150" = add i32 %".149", 1
  store i32 %".150", i32* %"t"
  %".152" = load i32, i32* %"t"
  %".153" = load i32, i32* %"index_1"
  %".154" = sub i32 %".153", 1
  store i32 %".154", i32* %"index_1"
  %".156" = load i32, i32* %"index_1"
  br label %".126"
.128:
  %".158" = load i32, i32* %"index_1"
  %".159" = add i32 %".158", 1
  store i32 %".159", i32* %"index_1"
  %".161" = load i32, i32* %"index_1"
  %".162" = load i32, i32* %"index_1"
  %".163" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".162"
  %".164" = load i32, i32* %"i"
  %".165" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".164"
  %".166" = load i8, i8* %".165"
  store i8 %".166", i8* %".163"
  %".168" = load i8, i8* %".163"
  %".169" = load i32, i32* %"i"
  %".170" = add i32 %".169", 1
  store i32 %".170", i32* %"i"
  %".172" = load i32, i32* %"i"
  br label %".110"
.174:
  br label %".192"
.175:
  br label %".243"
.176:
  br label %".110"
.192:
  %".196" = load i32, i32* %"index_1"
  %".197" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".196"
  %".198" = load i8, i8* %".197"
  %".199" = sext i8 %".198" to i32
  %".200" = icmp eq i32 %".199", 42
  %".201" = load i32, i32* %"index_1"
  %".202" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".201"
  %".203" = load i8, i8* %".202"
  %".204" = sext i8 %".203" to i32
  %".205" = icmp eq i32 %".204", 47
  %".206" = icmp ne i1 %".200", 0
  %".207" = icmp ne i1 %".205", 0
  %".208" = or i1 %".206", %".207"
  %".209" = icmp ne i1 %".208", 0
  br i1 %".209", label %".193", label %".194"
.193:
  %".211" = load i32, i32* %"t"
  %".212" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".211"
  %".213" = load i32, i32* %"index_1"
  %".214" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".213"
  %".215" = load i8, i8* %".214"
  store i8 %".215", i8* %".212"
  %".217" = load i8, i8* %".212"
  %".218" = load i32, i32* %"t"
  %".219" = add i32 %".218", 1
  store i32 %".219", i32* %"t"
  %".221" = load i32, i32* %"t"
  %".222" = load i32, i32* %"index_1"
  %".223" = sub i32 %".222", 1
  store i32 %".223", i32* %"index_1"
  %".225" = load i32, i32* %"index_1"
  br label %".192"
.194:
  %".227" = load i32, i32* %"index_1"
  %".228" = add i32 %".227", 1
  store i32 %".228", i32* %"index_1"
  %".230" = load i32, i32* %"index_1"
  %".231" = load i32, i32* %"index_1"
  %".232" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".231"
  %".233" = load i32, i32* %"i"
  %".234" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".233"
  %".235" = load i8, i8* %".234"
  store i8 %".235", i8* %".232"
  %".237" = load i8, i8* %".232"
  %".238" = load i32, i32* %"i"
  %".239" = add i32 %".238", 1
  store i32 %".239", i32* %"i"
  %".241" = load i32, i32* %"i"
  br label %".176"
.243:
  %".247" = load i32, i32* %"i"
  %".248" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".247"
  %".249" = load i8, i8* %".248"
  %".250" = sext i8 %".249" to i32
  %".251" = icmp sle i32 %".250", 57
  %".252" = load i32, i32* %"i"
  %".253" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".252"
  %".254" = load i8, i8* %".253"
  %".255" = sext i8 %".254" to i32
  %".256" = icmp sge i32 %".255", 48
  %".257" = icmp ne i1 %".251", 0
  %".258" = icmp ne i1 %".256", 0
  %".259" = and i1 %".257", %".258"
  %".260" = icmp ne i1 %".259", 0
  br i1 %".260", label %".244", label %".245"
.244:
  %".262" = load i32, i32* %"t"
  %".263" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".262"
  %".264" = load i32, i32* %"i"
  %".265" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".264"
  %".266" = load i8, i8* %".265"
  store i8 %".266", i8* %".263"
  %".268" = load i8, i8* %".263"
  %".269" = load i32, i32* %"t"
  %".270" = add i32 %".269", 1
  store i32 %".270", i32* %"t"
  %".272" = load i32, i32* %"t"
  %".273" = load i32, i32* %"i"
  %".274" = add i32 %".273", 1
  store i32 %".274", i32* %"i"
  %".276" = load i32, i32* %"i"
  br label %".243"
.245:
  %".278" = load i32, i32* %"t"
  %".279" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".278"
  %".280" = trunc i32 32 to i8
  store i8 %".280", i8* %".279"
  %".282" = load i8, i8* %".279"
  %".283" = load i32, i32* %"t"
  %".284" = add i32 %".283", 1
  store i32 %".284", i32* %"t"
  %".286" = load i32, i32* %"t"
  br label %".176"
.292:
  %".296" = load i32, i32* %"index_1"
  %".297" = icmp ne i32 %".296", 0
  %".298" = icmp ne i1 %".297", 0
  br i1 %".298", label %".293", label %".294"
.293:
  %".300" = load i32, i32* %"t"
  %".301" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".300"
  %".302" = load i32, i32* %"index_1"
  %".303" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".302"
  %".304" = load i8, i8* %".303"
  store i8 %".304", i8* %".301"
  %".306" = load i8, i8* %".301"
  %".307" = load i32, i32* %"t"
  %".308" = add i32 %".307", 1
  store i32 %".308", i32* %"t"
  %".310" = load i32, i32* %"t"
  %".311" = load i32, i32* %"index_1"
  %".312" = sub i32 %".311", 1
  store i32 %".312", i32* %"index_1"
  %".314" = load i32, i32* %"index_1"
  br label %".292"
.294:
  ret i32 0
}

@"__string_0" = internal global [22 x i8] c"strs the length is %d\00"
define i32 @"cal"()
{
__cal:
  %"stack" = alloca [100 x i32]
  %"index" = alloca i32
  %".2" = sub i32 0, 1
  store i32 %".2", i32* %"index"
  %"n_data" = alloca i32
  store i32 0, i32* %"n_data"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 0, i32* %"i"
  %".7" = load i32, i32* %"i"
  br label %".8"
.8:
  %".13" = load i32, i32* %"i"
  %".14" = icmp slt i32 %".13", 100
  %".15" = icmp ne i1 %".14", 0
  br i1 %".15", label %".9", label %".11"
.9:
  %".20" = load i32, i32* %"i"
  %".21" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".20"
  %".22" = load i8, i8* %".21"
  %".23" = sext i8 %".22" to i32
  %".24" = icmp sle i32 %".23", 57
  %".25" = load i32, i32* %"i"
  %".26" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".25"
  %".27" = load i8, i8* %".26"
  %".28" = sext i8 %".27" to i32
  %".29" = icmp sge i32 %".28", 48
  %".30" = icmp ne i1 %".24", 0
  %".31" = icmp ne i1 %".29", 0
  %".32" = and i1 %".30", %".31"
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %".17", label %".18"
.10:
  %".200" = load i32, i32* %"i"
  %".201" = add i32 %".200", 1
  store i32 %".201", i32* %"i"
  %".203" = load i32, i32* %"i"
  br label %".8"
.11:
  %".205" = load i32, i32* %"index"
  %".206" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".205"
  %".207" = load i32, i32* %".206"
  ret i32 %".207"
.17:
  %".35" = load i32, i32* %"n_data"
  %".36" = mul i32 %".35", 10
  %".37" = load i32, i32* %"i"
  %".38" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".37"
  %".39" = load i8, i8* %".38"
  %".40" = sext i8 %".39" to i32
  %".41" = sub i32 %".40", 48
  %".42" = add i32 %".36", %".41"
  store i32 %".42", i32* %"n_data"
  %".44" = load i32, i32* %"n_data"
  br label %".19"
.18:
  %".49" = load i32, i32* %"i"
  %".50" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".49"
  %".51" = load i8, i8* %".50"
  %".52" = sext i8 %".51" to i32
  %".53" = icmp eq i32 %".52", 32
  %".54" = icmp ne i1 %".53", 0
  br i1 %".54", label %".46", label %".47"
.19:
  br label %".10"
.46:
  %".56" = load i32, i32* %"index"
  %".57" = add i32 %".56", 1
  store i32 %".57", i32* %"index"
  %".59" = load i32, i32* %"index"
  %".60" = load i32, i32* %"index"
  %".61" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".60"
  %".62" = load i32, i32* %"n_data"
  store i32 %".62", i32* %".61"
  %".64" = load i32, i32* %".61"
  store i32 0, i32* %"n_data"
  %".66" = load i32, i32* %"n_data"
  br label %".48"
.47:
  %".71" = load i32, i32* %"i"
  %".72" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".71"
  %".73" = load i8, i8* %".72"
  %".74" = sext i8 %".73" to i32
  %".75" = icmp eq i32 %".74", 43
  %".76" = icmp ne i1 %".75", 0
  br i1 %".76", label %".68", label %".69"
.48:
  br label %".19"
.68:
  %".78" = load i32, i32* %"index"
  %".79" = sub i32 %".78", 1
  %".80" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".79"
  %".81" = load i32, i32* %"index"
  %".82" = sub i32 %".81", 1
  %".83" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".82"
  %".84" = load i32, i32* %".83"
  %".85" = load i32, i32* %"index"
  %".86" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".85"
  %".87" = load i32, i32* %".86"
  %".88" = add i32 %".84", %".87"
  store i32 %".88", i32* %".80"
  %".90" = load i32, i32* %".80"
  %".91" = load i32, i32* %"index"
  %".92" = sub i32 %".91", 1
  store i32 %".92", i32* %"index"
  %".94" = load i32, i32* %"index"
  br label %".70"
.69:
  %".99" = load i32, i32* %"i"
  %".100" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".99"
  %".101" = load i8, i8* %".100"
  %".102" = sext i8 %".101" to i32
  %".103" = icmp eq i32 %".102", 45
  %".104" = icmp ne i1 %".103", 0
  br i1 %".104", label %".96", label %".97"
.70:
  br label %".48"
.96:
  %".106" = load i32, i32* %"index"
  %".107" = sub i32 %".106", 1
  %".108" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".107"
  %".109" = load i32, i32* %"index"
  %".110" = sub i32 %".109", 1
  %".111" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".110"
  %".112" = load i32, i32* %".111"
  %".113" = load i32, i32* %"index"
  %".114" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".113"
  %".115" = load i32, i32* %".114"
  %".116" = sub i32 %".112", %".115"
  store i32 %".116", i32* %".108"
  %".118" = load i32, i32* %".108"
  %".119" = load i32, i32* %"index"
  %".120" = sub i32 %".119", 1
  store i32 %".120", i32* %"index"
  %".122" = load i32, i32* %"index"
  br label %".98"
.97:
  %".127" = load i32, i32* %"i"
  %".128" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".127"
  %".129" = load i8, i8* %".128"
  %".130" = sext i8 %".129" to i32
  %".131" = icmp eq i32 %".130", 42
  %".132" = icmp ne i1 %".131", 0
  br i1 %".132", label %".124", label %".125"
.98:
  br label %".70"
.124:
  %".134" = load i32, i32* %"index"
  %".135" = sub i32 %".134", 1
  %".136" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".135"
  %".137" = load i32, i32* %"index"
  %".138" = sub i32 %".137", 1
  %".139" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".138"
  %".140" = load i32, i32* %".139"
  %".141" = load i32, i32* %"index"
  %".142" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".141"
  %".143" = load i32, i32* %".142"
  %".144" = mul i32 %".140", %".143"
  store i32 %".144", i32* %".136"
  %".146" = load i32, i32* %".136"
  %".147" = load i32, i32* %"index"
  %".148" = sub i32 %".147", 1
  store i32 %".148", i32* %"index"
  %".150" = load i32, i32* %"index"
  br label %".126"
.125:
  %".154" = load i32, i32* %"i"
  %".155" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".154"
  %".156" = load i8, i8* %".155"
  %".157" = sext i8 %".156" to i32
  %".158" = icmp eq i32 %".157", 47
  %".159" = icmp ne i1 %".158", 0
  br i1 %".159", label %".152", label %".153"
.126:
  br label %".98"
.152:
  %".164" = load i32, i32* %"index"
  %".165" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".164"
  %".166" = load i32, i32* %".165"
  %".167" = icmp ne i32 %".166", 0
  %".168" = icmp ne i1 %".167", 0
  br i1 %".168", label %".161", label %".162"
.153:
  br label %".126"
.161:
  %".170" = load i32, i32* %"index"
  %".171" = sub i32 %".170", 1
  %".172" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".171"
  %".173" = load i32, i32* %"index"
  %".174" = sub i32 %".173", 1
  %".175" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".174"
  %".176" = load i32, i32* %".175"
  %".177" = load i32, i32* %"index"
  %".178" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".177"
  %".179" = load i32, i32* %".178"
  %".180" = add i32 %".176", %".179"
  store i32 %".180", i32* %".172"
  %".182" = load i32, i32* %".172"
  %".183" = load i32, i32* %"index"
  %".184" = sub i32 %".183", 1
  store i32 %".184", i32* %"index"
  %".186" = load i32, i32* %"index"
  br label %".163"
.162:
  %".188" = getelementptr inbounds [23 x i8], [23 x i8]* @"__string_1", i32 0, i32 0
  %".189" = call i32 (i8*, ...) @"printf"(i8* %".188")
  store i32 1, i32* @"judgezero"
  %".191" = load i32, i32* @"judgezero"
  ret i32 0
.163:
  br label %".153"
}

@"__string_1" = internal global [23 x i8] c"error:divisor is zero\0a\00"
define i32 @"judge"(i8 %".1")
{
__judge:
  %"c" = alloca i8
  store i8 %".1", i8* %"c"
  %"typejudge" = alloca i32
  %".4" = sub i32 0, 1
  store i32 %".4", i32* %"typejudge"
  %".9" = load i8, i8* %"c"
  %".10" = sext i8 %".9" to i32
  %".11" = icmp eq i32 %".10", 43
  %".12" = load i8, i8* %"c"
  %".13" = sext i8 %".12" to i32
  %".14" = icmp eq i32 %".13", 45
  %".15" = icmp ne i1 %".11", 0
  %".16" = icmp ne i1 %".14", 0
  %".17" = or i1 %".15", %".16"
  %".18" = load i8, i8* %"c"
  %".19" = sext i8 %".18" to i32
  %".20" = icmp eq i32 %".19", 42
  %".21" = icmp ne i1 %".17", 0
  %".22" = icmp ne i1 %".20", 0
  %".23" = or i1 %".21", %".22"
  %".24" = load i8, i8* %"c"
  %".25" = sext i8 %".24" to i32
  %".26" = icmp eq i32 %".25", 47
  %".27" = icmp ne i1 %".23", 0
  %".28" = icmp ne i1 %".26", 0
  %".29" = or i1 %".27", %".28"
  %".30" = icmp ne i1 %".29", 0
  br i1 %".30", label %".6", label %".7"
.6:
  store i32 1, i32* %"typejudge"
  %".33" = load i32, i32* %"typejudge"
  br label %".8"
.7:
  %".38" = load i8, i8* %"c"
  %".39" = sext i8 %".38" to i32
  %".40" = icmp sle i32 %".39", 57
  %".41" = load i8, i8* %"c"
  %".42" = sext i8 %".41" to i32
  %".43" = icmp sge i32 %".42", 48
  %".44" = icmp ne i1 %".40", 0
  %".45" = icmp ne i1 %".43", 0
  %".46" = and i1 %".44", %".45"
  %".47" = icmp ne i1 %".46", 0
  br i1 %".47", label %".35", label %".36"
.8:
  %".76" = load i32, i32* %"typejudge"
  ret i32 %".76"
.35:
  store i32 0, i32* %"typejudge"
  %".50" = load i32, i32* %"typejudge"
  br label %".37"
.36:
  %".55" = load i8, i8* %"c"
  %".56" = sext i8 %".55" to i32
  %".57" = icmp eq i32 %".56", 91
  %".58" = icmp ne i1 %".57", 0
  br i1 %".58", label %".52", label %".53"
.37:
  br label %".8"
.52:
  store i32 2, i32* %"typejudge"
  %".61" = load i32, i32* %"typejudge"
  br label %".54"
.53:
  %".65" = load i8, i8* %"c"
  %".66" = sext i8 %".65" to i32
  %".67" = icmp eq i32 %".66", 93
  %".68" = icmp ne i1 %".67", 0
  br i1 %".68", label %".63", label %".64"
.54:
  br label %".37"
.63:
  store i32 3, i32* %"typejudge"
  %".71" = load i32, i32* %"typejudge"
  br label %".64"
.64:
  br label %".54"
}

define i32 @"main"()
{
__main:
  store i32 0, i32* @"judgezero"
  %".3" = load i32, i32* @"judgezero"
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".5" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".4", i8* %".5")
  %"len" = alloca i32
  store i32 0, i32* %"len"
  store i32 0, i32* %"len"
  %".9" = load i32, i32* %"len"
  br label %".10"
.10:
  %".15" = load i32, i32* %"len"
  %".16" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".15"
  %".17" = load i8, i8* %".16"
  %".18" = sext i8 %".17" to i32
  %".19" = icmp ne i32 %".18", 0
  %".20" = icmp ne i1 %".19", 0
  br i1 %".20", label %".11", label %".13"
.11:
  br label %".12"
.12:
  %".23" = load i32, i32* %"len"
  %".24" = add i32 %".23", 1
  store i32 %".24", i32* %"len"
  br label %".10"
.13:
  %"left" = alloca i32
  store i32 0, i32* %"left"
  %"pst" = alloca i32
  %".28" = sub i32 0, 2
  store i32 %".28", i32* %"pst"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 0, i32* %"i"
  %".32" = load i32, i32* %"i"
  br label %".33"
.33:
  %".38" = load i32, i32* %"i"
  %".39" = load i32, i32* %"len"
  %".40" = icmp slt i32 %".38", %".39"
  %".41" = icmp ne i1 %".40", 0
  br i1 %".41", label %".34", label %".36"
.34:
  %"jud" = alloca i32
  %".43" = load i32, i32* %"i"
  %".44" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".43"
  %".45" = load i8, i8* %".44"
  %".46" = call i32 @"judge"(i8 %".45")
  store i32 %".46", i32* %"jud"
  %".51" = load i32, i32* %"jud"
  %".52" = icmp sge i32 %".51", 0
  %".53" = icmp ne i1 %".52", 0
  br i1 %".53", label %".48", label %".49"
.35:
  %".207" = load i32, i32* %"i"
  %".208" = add i32 %".207", 1
  store i32 %".208", i32* %"i"
  %".210" = load i32, i32* %"i"
  br label %".33"
.36:
  %".214" = load i32, i32* %"left"
  %".215" = icmp ne i32 %".214", 0
  %".216" = icmp ne i1 %".215", 0
  br i1 %".216", label %".212", label %".213"
.48:
  %".58" = load i32, i32* %"i"
  %".59" = icmp ne i32 %".58", 0
  %".60" = icmp ne i1 %".59", 0
  br i1 %".60", label %".55", label %".56"
.49:
  %".203" = getelementptr inbounds [24 x i8], [24 x i8]* @"__string_10", i32 0, i32 0
  %".204" = call i32 (i8*, ...) @"printf"(i8* %".203")
  ret i32 0
.50:
  br label %".35"
.55:
  %".65" = load i32, i32* %"pst"
  %".66" = icmp eq i32 %".65", 1
  %".67" = load i32, i32* %"jud"
  %".68" = icmp eq i32 %".67", 1
  %".69" = icmp ne i1 %".66", 0
  %".70" = icmp ne i1 %".68", 0
  %".71" = and i1 %".69", %".70"
  %".72" = icmp ne i1 %".71", 0
  br i1 %".72", label %".62", label %".63"
.56:
  %".146" = load i32, i32* %"jud"
  %".147" = icmp eq i32 %".146", 1
  %".148" = load i32, i32* %"jud"
  %".149" = icmp eq i32 %".148", 3
  %".150" = icmp ne i1 %".147", 0
  %".151" = icmp ne i1 %".149", 0
  %".152" = or i1 %".150", %".151"
  %".153" = icmp ne i1 %".152", 0
  br i1 %".153", label %".144", label %".145"
.57:
  %".165" = load i32, i32* %"jud"
  %".166" = icmp eq i32 %".165", 2
  %".167" = icmp ne i1 %".166", 0
  br i1 %".167", label %".162", label %".163"
.62:
  %".74" = getelementptr inbounds [30 x i8], [30 x i8]* @"__string_3", i32 0, i32 0
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".74")
  ret i32 0
.63:
  %".80" = load i32, i32* %"pst"
  %".81" = icmp eq i32 %".80", 2
  %".82" = load i32, i32* %"jud"
  %".83" = icmp ne i32 %".82", 0
  %".84" = icmp ne i1 %".81", 0
  %".85" = icmp ne i1 %".83", 0
  %".86" = and i1 %".84", %".85"
  %".87" = icmp ne i1 %".86", 0
  br i1 %".87", label %".77", label %".78"
.64:
  %".140" = load i32, i32* %"jud"
  store i32 %".140", i32* %"pst"
  %".142" = load i32, i32* %"pst"
  br label %".57"
.77:
  %".89" = getelementptr inbounds [42 x i8], [42 x i8]* @"__string_4", i32 0, i32 0
  %".90" = call i32 (i8*, ...) @"printf"(i8* %".89")
  ret i32 0
.78:
  %".95" = load i32, i32* %"pst"
  %".96" = icmp eq i32 %".95", 3
  %".97" = load i32, i32* %"jud"
  %".98" = icmp eq i32 %".97", 0
  %".99" = icmp ne i1 %".96", 0
  %".100" = icmp ne i1 %".98", 0
  %".101" = and i1 %".99", %".100"
  %".102" = icmp ne i1 %".101", 0
  br i1 %".102", label %".92", label %".93"
.79:
  br label %".64"
.92:
  %".104" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_5", i32 0, i32 0
  %".105" = call i32 (i8*, ...) @"printf"(i8* %".104")
  ret i32 0
.93:
  %".110" = load i32, i32* %"pst"
  %".111" = icmp eq i32 %".110", 0
  %".112" = load i32, i32* %"jud"
  %".113" = icmp eq i32 %".112", 2
  %".114" = icmp ne i1 %".111", 0
  %".115" = icmp ne i1 %".113", 0
  %".116" = and i1 %".114", %".115"
  %".117" = icmp ne i1 %".116", 0
  br i1 %".117", label %".107", label %".108"
.94:
  br label %".79"
.107:
  %".119" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_6", i32 0, i32 0
  %".120" = call i32 (i8*, ...) @"printf"(i8* %".119")
  ret i32 0
.108:
  %".124" = load i32, i32* %"pst"
  %".125" = icmp ne i32 %".124", 0
  %".126" = load i32, i32* %"jud"
  %".127" = icmp eq i32 %".126", 3
  %".128" = icmp ne i1 %".125", 0
  %".129" = icmp ne i1 %".127", 0
  %".130" = and i1 %".128", %".129"
  %".131" = icmp ne i1 %".130", 0
  br i1 %".131", label %".122", label %".123"
.109:
  br label %".94"
.122:
  %".133" = getelementptr inbounds [36 x i8], [36 x i8]* @"__string_7", i32 0, i32 0
  %".134" = call i32 (i8*, ...) @"printf"(i8* %".133")
  ret i32 0
.123:
  br label %".109"
.144:
  %".155" = getelementptr inbounds [49 x i8], [49 x i8]* @"__string_8", i32 0, i32 0
  %".156" = call i32 (i8*, ...) @"printf"(i8* %".155")
  ret i32 0
.145:
  %".158" = load i32, i32* %"jud"
  store i32 %".158", i32* %"pst"
  %".160" = load i32, i32* %"pst"
  br label %".57"
.162:
  %".169" = load i32, i32* %"left"
  %".170" = add i32 %".169", 1
  store i32 %".170", i32* %"left"
  %".172" = load i32, i32* %"left"
  br label %".164"
.163:
  %".176" = load i32, i32* %"jud"
  %".177" = icmp eq i32 %".176", 3
  %".178" = icmp ne i1 %".177", 0
  br i1 %".178", label %".174", label %".175"
.164:
  %".186" = load i32, i32* %"i"
  %".187" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".186"
  %".188" = load i32, i32* %"i"
  %".189" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".188"
  %".190" = load i8, i8* %".189"
  store i8 %".190", i8* %".187"
  %".192" = load i8, i8* %".187"
  %".195" = load i32, i32* %"left"
  %".196" = icmp slt i32 %".195", 0
  %".197" = icmp ne i1 %".196", 0
  br i1 %".197", label %".193", label %".194"
.174:
  %".180" = load i32, i32* %"left"
  %".181" = sub i32 %".180", 1
  store i32 %".181", i32* %"left"
  %".183" = load i32, i32* %"left"
  br label %".175"
.175:
  br label %".164"
.193:
  %".199" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_9", i32 0, i32 0
  %".200" = call i32 (i8*, ...) @"printf"(i8* %".199")
  ret i32 0
.194:
  br label %".50"
.212:
  %".218" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_11", i32 0, i32 0
  %".219" = call i32 (i8*, ...) @"printf"(i8* %".218")
  ret i32 0
.213:
  %".221" = call i32 @"Polish"()
  %"num" = alloca i32
  %".222" = call i32 @"cal"()
  store i32 %".222", i32* %"num"
  %".226" = load i32, i32* @"judgezero"
  %".227" = icmp eq i32 %".226", 1
  %".228" = icmp ne i1 %".227", 0
  br i1 %".228", label %".224", label %".225"
.224:
  ret i32 0
.225:
  %".231" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_12", i32 0, i32 0
  %".232" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 0
  %".233" = call i32 (i8*, ...) @"printf"(i8* %".231", i8* %".232")
  %".234" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_13", i32 0, i32 0
  %".235" = load i32, i32* %"num"
  %".236" = call i32 (i8*, ...) @"printf"(i8* %".234", i32 %".235")
  ret i32 0
}

@"__string_2" = internal global [3 x i8] c"%s\00"
@"__string_3" = internal global [30 x i8] c"error:input 2 continuous ops\0a\00"
@"__string_4" = internal global [42 x i8] c"error:input '[' without following number\0a\00"
@"__string_5" = internal global [39 x i8] c"error:input ']' with following number\0a\00"
@"__string_6" = internal global [39 x i8] c"error:input number with following '['\0a\00"
@"__string_7" = internal global [36 x i8] c"error:before ']' there's no number\0a\00"
@"__string_8" = internal global [49 x i8] c"error:expression cannot start with an op or ']'\0a\00"
@"__string_9" = internal global [20 x i8] c"error:unmatched []\0a\00"
@"__string_10" = internal global [24 x i8] c"error:input unaccepted\0a\00"
@"__string_11" = internal global [20 x i8] c"error:unmatched []\0a\00"
@"__string_12" = internal global [4 x i8] c"%s\0a\00"
@"__string_13" = internal global [4 x i8] c"%d\0a\00"