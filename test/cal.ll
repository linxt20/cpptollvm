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
  %"t" = alloca i32
  store i32 0, i32* %"t"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %".26"
.26:
  %".30" = load i32, i32* %"i"
  %".31" = load i32, i32* %"len"
  %".32" = icmp slt i32 %".30", %".31"
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %".27", label %".28"
.27:
  %".38" = load i32, i32* %"i"
  %".39" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".38"
  %".40" = load i8, i8* %".39"
  %".41" = sext i8 %".40" to i32
  %".42" = icmp eq i32 %".41", 91
  %".43" = icmp ne i1 %".42", 0
  br i1 %".43", label %".35", label %".36"
.28:
  br label %".289"
.35:
  %".45" = load i32, i32* %"index_1"
  %".46" = add i32 %".45", 1
  store i32 %".46", i32* %"index_1"
  %".48" = load i32, i32* %"index_1"
  %".49" = load i32, i32* %"index_1"
  %".50" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".49"
  %".51" = trunc i32 91 to i8
  store i8 %".51", i8* %".50"
  %".53" = load i8, i8* %".50"
  %".54" = load i32, i32* %"i"
  %".55" = add i32 %".54", 1
  store i32 %".55", i32* %"i"
  %".57" = load i32, i32* %"i"
  br label %".37"
.36:
  %".62" = load i32, i32* %"i"
  %".63" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".62"
  %".64" = load i8, i8* %".63"
  %".65" = sext i8 %".64" to i32
  %".66" = icmp eq i32 %".65", 93
  %".67" = icmp ne i1 %".66", 0
  br i1 %".67", label %".59", label %".60"
.37:
  br label %".26"
.59:
  br label %".69"
.60:
  %".108" = load i32, i32* %"i"
  %".109" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".108"
  %".110" = load i8, i8* %".109"
  %".111" = sext i8 %".110" to i32
  %".112" = icmp eq i32 %".111", 43
  %".113" = load i32, i32* %"i"
  %".114" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".113"
  %".115" = load i8, i8* %".114"
  %".116" = sext i8 %".115" to i32
  %".117" = icmp eq i32 %".116", 45
  %".118" = icmp ne i1 %".112", 0
  %".119" = icmp ne i1 %".117", 0
  %".120" = or i1 %".118", %".119"
  %".121" = icmp ne i1 %".120", 0
  br i1 %".121", label %".105", label %".106"
.61:
  br label %".37"
.69:
  %".73" = load i32, i32* %"index_1"
  %".74" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".73"
  %".75" = load i8, i8* %".74"
  %".76" = sext i8 %".75" to i32
  %".77" = icmp ne i32 %".76", 91
  %".78" = icmp ne i1 %".77", 0
  br i1 %".78", label %".70", label %".71"
.70:
  %".80" = load i32, i32* %"t"
  %".81" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".80"
  %".82" = load i32, i32* %"index_1"
  %".83" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".82"
  %".84" = load i8, i8* %".83"
  store i8 %".84", i8* %".81"
  %".86" = load i8, i8* %".81"
  %".87" = load i32, i32* %"t"
  %".88" = add i32 %".87", 1
  store i32 %".88", i32* %"t"
  %".90" = load i32, i32* %"t"
  %".91" = load i32, i32* %"index_1"
  %".92" = sub i32 %".91", 1
  store i32 %".92", i32* %"index_1"
  %".94" = load i32, i32* %"index_1"
  br label %".69"
.71:
  %".96" = load i32, i32* %"index_1"
  %".97" = sub i32 %".96", 1
  store i32 %".97", i32* %"index_1"
  %".99" = load i32, i32* %"index_1"
  %".100" = load i32, i32* %"i"
  %".101" = add i32 %".100", 1
  store i32 %".101", i32* %"i"
  %".103" = load i32, i32* %"i"
  br label %".61"
.105:
  br label %".123"
.106:
  %".174" = load i32, i32* %"i"
  %".175" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".174"
  %".176" = load i8, i8* %".175"
  %".177" = sext i8 %".176" to i32
  %".178" = icmp eq i32 %".177", 42
  %".179" = load i32, i32* %"i"
  %".180" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".179"
  %".181" = load i8, i8* %".180"
  %".182" = sext i8 %".181" to i32
  %".183" = icmp eq i32 %".182", 47
  %".184" = icmp ne i1 %".178", 0
  %".185" = icmp ne i1 %".183", 0
  %".186" = or i1 %".184", %".185"
  %".187" = icmp ne i1 %".186", 0
  br i1 %".187", label %".171", label %".172"
.107:
  br label %".61"
.123:
  %".127" = load i32, i32* %"index_1"
  %".128" = icmp ne i32 %".127", 0
  %".129" = load i32, i32* %"index_1"
  %".130" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".129"
  %".131" = load i8, i8* %".130"
  %".132" = sext i8 %".131" to i32
  %".133" = icmp ne i32 %".132", 91
  %".134" = icmp ne i1 %".128", 0
  %".135" = icmp ne i1 %".133", 0
  %".136" = and i1 %".134", %".135"
  %".137" = icmp ne i1 %".136", 0
  br i1 %".137", label %".124", label %".125"
.124:
  %".139" = load i32, i32* %"t"
  %".140" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".139"
  %".141" = load i32, i32* %"index_1"
  %".142" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".141"
  %".143" = load i8, i8* %".142"
  store i8 %".143", i8* %".140"
  %".145" = load i8, i8* %".140"
  %".146" = load i32, i32* %"t"
  %".147" = add i32 %".146", 1
  store i32 %".147", i32* %"t"
  %".149" = load i32, i32* %"t"
  %".150" = load i32, i32* %"index_1"
  %".151" = sub i32 %".150", 1
  store i32 %".151", i32* %"index_1"
  %".153" = load i32, i32* %"index_1"
  br label %".123"
.125:
  %".155" = load i32, i32* %"index_1"
  %".156" = add i32 %".155", 1
  store i32 %".156", i32* %"index_1"
  %".158" = load i32, i32* %"index_1"
  %".159" = load i32, i32* %"index_1"
  %".160" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".159"
  %".161" = load i32, i32* %"i"
  %".162" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".161"
  %".163" = load i8, i8* %".162"
  store i8 %".163", i8* %".160"
  %".165" = load i8, i8* %".160"
  %".166" = load i32, i32* %"i"
  %".167" = add i32 %".166", 1
  store i32 %".167", i32* %"i"
  %".169" = load i32, i32* %"i"
  br label %".107"
.171:
  br label %".189"
.172:
  br label %".240"
.173:
  br label %".107"
.189:
  %".193" = load i32, i32* %"index_1"
  %".194" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".193"
  %".195" = load i8, i8* %".194"
  %".196" = sext i8 %".195" to i32
  %".197" = icmp eq i32 %".196", 42
  %".198" = load i32, i32* %"index_1"
  %".199" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".198"
  %".200" = load i8, i8* %".199"
  %".201" = sext i8 %".200" to i32
  %".202" = icmp eq i32 %".201", 47
  %".203" = icmp ne i1 %".197", 0
  %".204" = icmp ne i1 %".202", 0
  %".205" = or i1 %".203", %".204"
  %".206" = icmp ne i1 %".205", 0
  br i1 %".206", label %".190", label %".191"
.190:
  %".208" = load i32, i32* %"t"
  %".209" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".208"
  %".210" = load i32, i32* %"index_1"
  %".211" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".210"
  %".212" = load i8, i8* %".211"
  store i8 %".212", i8* %".209"
  %".214" = load i8, i8* %".209"
  %".215" = load i32, i32* %"t"
  %".216" = add i32 %".215", 1
  store i32 %".216", i32* %"t"
  %".218" = load i32, i32* %"t"
  %".219" = load i32, i32* %"index_1"
  %".220" = sub i32 %".219", 1
  store i32 %".220", i32* %"index_1"
  %".222" = load i32, i32* %"index_1"
  br label %".189"
.191:
  %".224" = load i32, i32* %"index_1"
  %".225" = add i32 %".224", 1
  store i32 %".225", i32* %"index_1"
  %".227" = load i32, i32* %"index_1"
  %".228" = load i32, i32* %"index_1"
  %".229" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".228"
  %".230" = load i32, i32* %"i"
  %".231" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".230"
  %".232" = load i8, i8* %".231"
  store i8 %".232", i8* %".229"
  %".234" = load i8, i8* %".229"
  %".235" = load i32, i32* %"i"
  %".236" = add i32 %".235", 1
  store i32 %".236", i32* %"i"
  %".238" = load i32, i32* %"i"
  br label %".173"
.240:
  %".244" = load i32, i32* %"i"
  %".245" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".244"
  %".246" = load i8, i8* %".245"
  %".247" = sext i8 %".246" to i32
  %".248" = icmp sle i32 %".247", 57
  %".249" = load i32, i32* %"i"
  %".250" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".249"
  %".251" = load i8, i8* %".250"
  %".252" = sext i8 %".251" to i32
  %".253" = icmp sge i32 %".252", 48
  %".254" = icmp ne i1 %".248", 0
  %".255" = icmp ne i1 %".253", 0
  %".256" = and i1 %".254", %".255"
  %".257" = icmp ne i1 %".256", 0
  br i1 %".257", label %".241", label %".242"
.241:
  %".259" = load i32, i32* %"t"
  %".260" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".259"
  %".261" = load i32, i32* %"i"
  %".262" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".261"
  %".263" = load i8, i8* %".262"
  store i8 %".263", i8* %".260"
  %".265" = load i8, i8* %".260"
  %".266" = load i32, i32* %"t"
  %".267" = add i32 %".266", 1
  store i32 %".267", i32* %"t"
  %".269" = load i32, i32* %"t"
  %".270" = load i32, i32* %"i"
  %".271" = add i32 %".270", 1
  store i32 %".271", i32* %"i"
  %".273" = load i32, i32* %"i"
  br label %".240"
.242:
  %".275" = load i32, i32* %"t"
  %".276" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".275"
  %".277" = trunc i32 32 to i8
  store i8 %".277", i8* %".276"
  %".279" = load i8, i8* %".276"
  %".280" = load i32, i32* %"t"
  %".281" = add i32 %".280", 1
  store i32 %".281", i32* %"t"
  %".283" = load i32, i32* %"t"
  br label %".173"
.289:
  %".293" = load i32, i32* %"index_1"
  %".294" = icmp ne i32 %".293", 0
  %".295" = icmp ne i1 %".294", 0
  br i1 %".295", label %".290", label %".291"
.290:
  %".297" = load i32, i32* %"t"
  %".298" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".297"
  %".299" = load i32, i32* %"index_1"
  %".300" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".299"
  %".301" = load i8, i8* %".300"
  store i8 %".301", i8* %".298"
  %".303" = load i8, i8* %".298"
  %".304" = load i32, i32* %"t"
  %".305" = add i32 %".304", 1
  store i32 %".305", i32* %"t"
  %".307" = load i32, i32* %"t"
  %".308" = load i32, i32* %"index_1"
  %".309" = sub i32 %".308", 1
  store i32 %".309", i32* %"index_1"
  %".311" = load i32, i32* %"index_1"
  br label %".289"
.291:
  ret i32 0
}

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
  %".180" = sdiv i32 %".176", %".179"
  store i32 %".180", i32* %".172"
  %".182" = load i32, i32* %".172"
  %".183" = load i32, i32* %"index"
  %".184" = sub i32 %".183", 1
  store i32 %".184", i32* %"index"
  %".186" = load i32, i32* %"index"
  br label %".163"
.162:
  %".188" = getelementptr inbounds [23 x i8], [23 x i8]* @"__string_0", i32 0, i32 0
  %".189" = call i32 (i8*, ...) @"printf"(i8* %".188")
  store i32 1, i32* @"judgezero"
  %".191" = load i32, i32* @"judgezero"
  ret i32 0
.163:
  br label %".153"
}

@"__string_0" = internal global [23 x i8] c"error:divisor is zero\0a\00"
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
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_1", i32 0, i32 0
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
  %".203" = getelementptr inbounds [24 x i8], [24 x i8]* @"__string_9", i32 0, i32 0
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
  %".74" = getelementptr inbounds [30 x i8], [30 x i8]* @"__string_2", i32 0, i32 0
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
  %".89" = getelementptr inbounds [42 x i8], [42 x i8]* @"__string_3", i32 0, i32 0
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
  %".104" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_4", i32 0, i32 0
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
  %".119" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_5", i32 0, i32 0
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
  %".133" = getelementptr inbounds [36 x i8], [36 x i8]* @"__string_6", i32 0, i32 0
  %".134" = call i32 (i8*, ...) @"printf"(i8* %".133")
  ret i32 0
.123:
  br label %".109"
.144:
  %".155" = getelementptr inbounds [49 x i8], [49 x i8]* @"__string_7", i32 0, i32 0
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
  %".199" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_8", i32 0, i32 0
  %".200" = call i32 (i8*, ...) @"printf"(i8* %".199")
  ret i32 0
.194:
  br label %".50"
.212:
  %".218" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_10", i32 0, i32 0
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
  %".231" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_11", i32 0, i32 0
  %".232" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 0
  %".233" = call i32 (i8*, ...) @"printf"(i8* %".231", i8* %".232")
  %".234" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_12", i32 0, i32 0
  %".235" = load i32, i32* %"num"
  %".236" = call i32 (i8*, ...) @"printf"(i8* %".234", i32 %".235")
  ret i32 0
}

@"__string_1" = internal global [3 x i8] c"%s\00"
@"__string_2" = internal global [30 x i8] c"error:input 2 continuous ops\0a\00"
@"__string_3" = internal global [42 x i8] c"error:input '[' without following number\0a\00"
@"__string_4" = internal global [39 x i8] c"error:input ']' with following number\0a\00"
@"__string_5" = internal global [39 x i8] c"error:input number with following '['\0a\00"
@"__string_6" = internal global [36 x i8] c"error:before ']' there's no number\0a\00"
@"__string_7" = internal global [49 x i8] c"error:expression cannot start with an op or ']'\0a\00"
@"__string_8" = internal global [20 x i8] c"error:unmatched []\0a\00"
@"__string_9" = internal global [24 x i8] c"error:input unaccepted\0a\00"
@"__string_10" = internal global [20 x i8] c"error:unmatched []\0a\00"
@"__string_11" = internal global [4 x i8] c"%s\0a\00"
@"__string_12" = internal global [4 x i8] c"%d\0a\00"