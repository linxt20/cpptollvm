; ModuleID = "cal.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"final" = internal global [100 x i8] zeroinitializer
@"strs" = internal global [100 x i8] zeroinitializer
@"stringone" = internal global [100 x i8] zeroinitializer
@"judgezero" = internal global i32 0
define void @"Polish"()
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
  %".14" = icmp ne i8 %".13", 92
  %".15" = icmp ne i1 %".14", 0
  br i1 %".15", label %".7", label %".9"
.7:
  br label %".8"
.8:
  %".18" = load i32, i32* %"len"
  %".19" = add i32 %".18", 1
  store i32 %".19", i32* %"len"
  %".21" = load i32, i32* %"len"
  br label %".6"
.9:
  %"t" = alloca i32
  store i32 1, i32* %"t"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %".25"
.25:
  %".29" = load i32, i32* %"i"
  %".30" = load i32, i32* %"len"
  %".31" = icmp slt i32 %".29", %".30"
  %".32" = icmp ne i1 %".31", 0
  br i1 %".32", label %".26", label %".27"
.26:
  %".37" = load i32, i32* %"i"
  %".38" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".37"
  %".39" = load i8, i8* %".38"
  %".40" = icmp eq i8 %".39", 91
  %".41" = icmp ne i1 %".40", 0
  br i1 %".41", label %".34", label %".35"
.27:
  br label %".274"
.34:
  %".43" = load i32, i32* %"index_1"
  %".44" = add i32 %".43", 1
  store i32 %".44", i32* %"index_1"
  %".46" = load i32, i32* %"index_1"
  %".47" = load i32, i32* %"index_1"
  %".48" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".47"
  store i8 91, i8* %".48"
  %".50" = load i8, i8* %".48"
  %".51" = load i32, i32* %"i"
  %".52" = add i32 %".51", 1
  store i32 %".52", i32* %"i"
  %".54" = load i32, i32* %"i"
  br label %".36"
.35:
  %".59" = load i32, i32* %"i"
  %".60" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".59"
  %".61" = load i8, i8* %".60"
  %".62" = icmp eq i8 %".61", 93
  %".63" = icmp ne i1 %".62", 0
  br i1 %".63", label %".56", label %".57"
.36:
  br label %".25"
.56:
  br label %".65"
.57:
  %".103" = load i32, i32* %"i"
  %".104" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".103"
  %".105" = load i8, i8* %".104"
  %".106" = icmp eq i8 %".105", 43
  %".107" = load i32, i32* %"i"
  %".108" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".107"
  %".109" = load i8, i8* %".108"
  %".110" = icmp eq i8 %".109", 45
  %".111" = icmp ne i1 %".106", 0
  %".112" = icmp ne i1 %".110", 0
  %".113" = or i1 %".111", %".112"
  %".114" = icmp ne i1 %".113", 0
  br i1 %".114", label %".100", label %".101"
.58:
  br label %".36"
.65:
  %".69" = load i32, i32* %"index_1"
  %".70" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".69"
  %".71" = load i8, i8* %".70"
  %".72" = icmp ne i8 %".71", 91
  %".73" = icmp ne i1 %".72", 0
  br i1 %".73", label %".66", label %".67"
.66:
  %".75" = load i32, i32* %"t"
  %".76" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".75"
  %".77" = load i32, i32* %"index_1"
  %".78" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".77"
  %".79" = load i8, i8* %".78"
  store i8 %".79", i8* %".76"
  %".81" = load i8, i8* %".76"
  %".82" = load i32, i32* %"t"
  %".83" = add i32 %".82", 1
  store i32 %".83", i32* %"t"
  %".85" = load i32, i32* %"t"
  %".86" = load i32, i32* %"index_1"
  %".87" = sub i32 %".86", 1
  store i32 %".87", i32* %"index_1"
  %".89" = load i32, i32* %"index_1"
  br label %".65"
.67:
  %".91" = load i32, i32* %"index_1"
  %".92" = sub i32 %".91", 1
  store i32 %".92", i32* %"index_1"
  %".94" = load i32, i32* %"index_1"
  %".95" = load i32, i32* %"i"
  %".96" = add i32 %".95", 1
  store i32 %".96", i32* %"i"
  %".98" = load i32, i32* %"i"
  br label %".58"
.100:
  br label %".116"
.101:
  %".166" = load i32, i32* %"i"
  %".167" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".166"
  %".168" = load i8, i8* %".167"
  %".169" = icmp eq i8 %".168", 42
  %".170" = load i32, i32* %"i"
  %".171" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".170"
  %".172" = load i8, i8* %".171"
  %".173" = icmp eq i8 %".172", 47
  %".174" = icmp ne i1 %".169", 0
  %".175" = icmp ne i1 %".173", 0
  %".176" = or i1 %".174", %".175"
  %".177" = icmp ne i1 %".176", 0
  br i1 %".177", label %".163", label %".164"
.102:
  br label %".58"
.116:
  %".120" = load i32, i32* %"index_1"
  %".121" = icmp ne i32 %".120", 0
  %".122" = load i32, i32* %"index_1"
  %".123" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".122"
  %".124" = load i8, i8* %".123"
  %".125" = icmp ne i8 %".124", 91
  %".126" = icmp ne i1 %".121", 0
  %".127" = icmp ne i1 %".125", 0
  %".128" = and i1 %".126", %".127"
  %".129" = icmp ne i1 %".128", 0
  br i1 %".129", label %".117", label %".118"
.117:
  %".131" = load i32, i32* %"t"
  %".132" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".131"
  %".133" = load i32, i32* %"index_1"
  %".134" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".133"
  %".135" = load i8, i8* %".134"
  store i8 %".135", i8* %".132"
  %".137" = load i8, i8* %".132"
  %".138" = load i32, i32* %"t"
  %".139" = add i32 %".138", 1
  store i32 %".139", i32* %"t"
  %".141" = load i32, i32* %"t"
  %".142" = load i32, i32* %"index_1"
  %".143" = sub i32 %".142", 1
  store i32 %".143", i32* %"index_1"
  %".145" = load i32, i32* %"index_1"
  br label %".116"
.118:
  %".147" = load i32, i32* %"index_1"
  %".148" = add i32 %".147", 1
  store i32 %".148", i32* %"index_1"
  %".150" = load i32, i32* %"index_1"
  %".151" = load i32, i32* %"index_1"
  %".152" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".151"
  %".153" = load i32, i32* %"i"
  %".154" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".153"
  %".155" = load i8, i8* %".154"
  store i8 %".155", i8* %".152"
  %".157" = load i8, i8* %".152"
  %".158" = load i32, i32* %"i"
  %".159" = add i32 %".158", 1
  store i32 %".159", i32* %"i"
  %".161" = load i32, i32* %"i"
  br label %".102"
.163:
  br label %".179"
.164:
  br label %".228"
.165:
  br label %".102"
.179:
  %".183" = load i32, i32* %"index_1"
  %".184" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".183"
  %".185" = load i8, i8* %".184"
  %".186" = icmp eq i8 %".185", 42
  %".187" = load i32, i32* %"index_1"
  %".188" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".187"
  %".189" = load i8, i8* %".188"
  %".190" = icmp eq i8 %".189", 47
  %".191" = icmp ne i1 %".186", 0
  %".192" = icmp ne i1 %".190", 0
  %".193" = or i1 %".191", %".192"
  %".194" = icmp ne i1 %".193", 0
  br i1 %".194", label %".180", label %".181"
.180:
  %".196" = load i32, i32* %"t"
  %".197" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".196"
  %".198" = load i32, i32* %"index_1"
  %".199" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".198"
  %".200" = load i8, i8* %".199"
  store i8 %".200", i8* %".197"
  %".202" = load i8, i8* %".197"
  %".203" = load i32, i32* %"t"
  %".204" = add i32 %".203", 1
  store i32 %".204", i32* %"t"
  %".206" = load i32, i32* %"t"
  %".207" = load i32, i32* %"index_1"
  %".208" = sub i32 %".207", 1
  store i32 %".208", i32* %"index_1"
  %".210" = load i32, i32* %"index_1"
  br label %".179"
.181:
  %".212" = load i32, i32* %"index_1"
  %".213" = add i32 %".212", 1
  store i32 %".213", i32* %"index_1"
  %".215" = load i32, i32* %"index_1"
  %".216" = load i32, i32* %"index_1"
  %".217" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".216"
  %".218" = load i32, i32* %"i"
  %".219" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".218"
  %".220" = load i8, i8* %".219"
  store i8 %".220", i8* %".217"
  %".222" = load i8, i8* %".217"
  %".223" = load i32, i32* %"i"
  %".224" = add i32 %".223", 1
  store i32 %".224", i32* %"i"
  %".226" = load i32, i32* %"i"
  br label %".165"
.228:
  %".232" = load i32, i32* %"i"
  %".233" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".232"
  %".234" = load i8, i8* %".233"
  %".235" = icmp sle i8 %".234", 57
  %".236" = load i32, i32* %"i"
  %".237" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".236"
  %".238" = load i8, i8* %".237"
  %".239" = icmp sge i8 %".238", 48
  %".240" = icmp ne i1 %".235", 0
  %".241" = icmp ne i1 %".239", 0
  %".242" = and i1 %".240", %".241"
  %".243" = icmp ne i1 %".242", 0
  br i1 %".243", label %".229", label %".230"
.229:
  %".245" = load i32, i32* %"t"
  %".246" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".245"
  %".247" = load i32, i32* %"i"
  %".248" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".247"
  %".249" = load i8, i8* %".248"
  store i8 %".249", i8* %".246"
  %".251" = load i8, i8* %".246"
  %".252" = load i32, i32* %"t"
  %".253" = add i32 %".252", 1
  store i32 %".253", i32* %"t"
  %".255" = load i32, i32* %"t"
  %".256" = load i32, i32* %"i"
  %".257" = add i32 %".256", 1
  store i32 %".257", i32* %"i"
  %".259" = load i32, i32* %"i"
  br label %".228"
.230:
  %".261" = load i32, i32* %"t"
  %".262" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".261"
  store i8 32, i8* %".262"
  %".264" = load i8, i8* %".262"
  %".265" = load i32, i32* %"t"
  %".266" = add i32 %".265", 1
  store i32 %".266", i32* %"t"
  %".268" = load i32, i32* %"t"
  br label %".165"
.274:
  %".278" = load i32, i32* %"index_1"
  %".279" = icmp ne i32 %".278", 0
  %".280" = icmp ne i1 %".279", 0
  br i1 %".280", label %".275", label %".276"
.275:
  %".282" = load i32, i32* %"t"
  %".283" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".282"
  %".284" = load i32, i32* %"index_1"
  %".285" = getelementptr inbounds [100 x i8], [100 x i8]* %"s1", i32 0, i32 %".284"
  %".286" = load i8, i8* %".285"
  store i8 %".286", i8* %".283"
  %".288" = load i8, i8* %".283"
  %".289" = load i32, i32* %"t"
  %".290" = add i32 %".289", 1
  store i32 %".290", i32* %"t"
  %".292" = load i32, i32* %"t"
  %".293" = load i32, i32* %"index_1"
  %".294" = sub i32 %".293", 1
  store i32 %".294", i32* %"index_1"
  %".296" = load i32, i32* %"index_1"
  br label %".274"
.276:
  ret void
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
  %".23" = icmp sle i8 %".22", 57
  %".24" = load i32, i32* %"i"
  %".25" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".24"
  %".26" = load i8, i8* %".25"
  %".27" = icmp sge i8 %".26", 48
  %".28" = icmp ne i1 %".23", 0
  %".29" = icmp ne i1 %".27", 0
  %".30" = and i1 %".28", %".29"
  %".31" = icmp ne i1 %".30", 0
  br i1 %".31", label %".17", label %".18"
.10:
  %".193" = load i32, i32* %"i"
  %".194" = add i32 %".193", 1
  store i32 %".194", i32* %"i"
  %".196" = load i32, i32* %"i"
  br label %".8"
.11:
  %".198" = load i32, i32* %"index"
  %".199" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".198"
  %".200" = load i32, i32* %".199"
  ret i32 %".200"
.17:
  %".33" = load i32, i32* %"n_data"
  %".34" = mul i32 %".33", 10
  %".35" = load i32, i32* %"i"
  %".36" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".35"
  %".37" = load i8, i8* %".36"
  %".38" = sub i8 %".37", 48
  %".39" = sext i8 %".38" to i32
  %".40" = add i32 %".34", %".39"
  store i32 %".40", i32* %"n_data"
  %".42" = load i32, i32* %"n_data"
  br label %".19"
.18:
  %".47" = load i32, i32* %"i"
  %".48" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".47"
  %".49" = load i8, i8* %".48"
  %".50" = icmp eq i8 %".49", 32
  %".51" = icmp ne i1 %".50", 0
  br i1 %".51", label %".44", label %".45"
.19:
  br label %".10"
.44:
  %".53" = load i32, i32* %"index"
  %".54" = add i32 %".53", 1
  store i32 %".54", i32* %"index"
  %".56" = load i32, i32* %"index"
  %".57" = load i32, i32* %"index"
  %".58" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".57"
  %".59" = load i32, i32* %"n_data"
  store i32 %".59", i32* %".58"
  %".61" = load i32, i32* %".58"
  store i32 0, i32* %"n_data"
  %".63" = load i32, i32* %"n_data"
  br label %".46"
.45:
  %".68" = load i32, i32* %"i"
  %".69" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".68"
  %".70" = load i8, i8* %".69"
  %".71" = icmp eq i8 %".70", 43
  %".72" = icmp ne i1 %".71", 0
  br i1 %".72", label %".65", label %".66"
.46:
  br label %".19"
.65:
  %".74" = load i32, i32* %"index"
  %".75" = sub i32 %".74", 1
  %".76" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".75"
  %".77" = load i32, i32* %"index"
  %".78" = sub i32 %".77", 1
  %".79" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".78"
  %".80" = load i32, i32* %".79"
  %".81" = load i32, i32* %"index"
  %".82" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".81"
  %".83" = load i32, i32* %".82"
  %".84" = add i32 %".80", %".83"
  store i32 %".84", i32* %".76"
  %".86" = load i32, i32* %".76"
  %".87" = load i32, i32* %"index"
  %".88" = sub i32 %".87", 1
  store i32 %".88", i32* %"index"
  %".90" = load i32, i32* %"index"
  br label %".67"
.66:
  %".95" = load i32, i32* %"i"
  %".96" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".95"
  %".97" = load i8, i8* %".96"
  %".98" = icmp eq i8 %".97", 45
  %".99" = icmp ne i1 %".98", 0
  br i1 %".99", label %".92", label %".93"
.67:
  br label %".46"
.92:
  %".101" = load i32, i32* %"index"
  %".102" = sub i32 %".101", 1
  %".103" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".102"
  %".104" = load i32, i32* %"index"
  %".105" = sub i32 %".104", 1
  %".106" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".105"
  %".107" = load i32, i32* %".106"
  %".108" = load i32, i32* %"index"
  %".109" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".108"
  %".110" = load i32, i32* %".109"
  %".111" = sub i32 %".107", %".110"
  store i32 %".111", i32* %".103"
  %".113" = load i32, i32* %".103"
  %".114" = load i32, i32* %"index"
  %".115" = sub i32 %".114", 1
  store i32 %".115", i32* %"index"
  %".117" = load i32, i32* %"index"
  br label %".94"
.93:
  %".122" = load i32, i32* %"i"
  %".123" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".122"
  %".124" = load i8, i8* %".123"
  %".125" = icmp eq i8 %".124", 42
  %".126" = icmp ne i1 %".125", 0
  br i1 %".126", label %".119", label %".120"
.94:
  br label %".67"
.119:
  %".128" = load i32, i32* %"index"
  %".129" = sub i32 %".128", 1
  %".130" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".129"
  %".131" = load i32, i32* %"index"
  %".132" = sub i32 %".131", 1
  %".133" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".132"
  %".134" = load i32, i32* %".133"
  %".135" = load i32, i32* %"index"
  %".136" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".135"
  %".137" = load i32, i32* %".136"
  %".138" = mul i32 %".134", %".137"
  store i32 %".138", i32* %".130"
  %".140" = load i32, i32* %".130"
  %".141" = load i32, i32* %"index"
  %".142" = sub i32 %".141", 1
  store i32 %".142", i32* %"index"
  %".144" = load i32, i32* %"index"
  br label %".121"
.120:
  %".148" = load i32, i32* %"i"
  %".149" = getelementptr inbounds [100 x i8], [100 x i8]* @"final", i32 0, i32 %".148"
  %".150" = load i8, i8* %".149"
  %".151" = icmp eq i8 %".150", 47
  %".152" = icmp ne i1 %".151", 0
  br i1 %".152", label %".146", label %".147"
.121:
  br label %".94"
.146:
  %".157" = load i32, i32* %"index"
  %".158" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".157"
  %".159" = load i32, i32* %".158"
  %".160" = icmp ne i32 %".159", 0
  %".161" = icmp ne i1 %".160", 0
  br i1 %".161", label %".154", label %".155"
.147:
  br label %".121"
.154:
  %".163" = load i32, i32* %"index"
  %".164" = sub i32 %".163", 1
  %".165" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".164"
  %".166" = load i32, i32* %"index"
  %".167" = sub i32 %".166", 1
  %".168" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".167"
  %".169" = load i32, i32* %".168"
  %".170" = load i32, i32* %"index"
  %".171" = getelementptr inbounds [100 x i32], [100 x i32]* %"stack", i32 0, i32 %".170"
  %".172" = load i32, i32* %".171"
  %".173" = add i32 %".169", %".172"
  store i32 %".173", i32* %".165"
  %".175" = load i32, i32* %".165"
  %".176" = load i32, i32* %"index"
  %".177" = sub i32 %".176", 1
  store i32 %".177", i32* %"index"
  %".179" = load i32, i32* %"index"
  br label %".156"
.155:
  %".181" = getelementptr inbounds [23 x i8], [23 x i8]* @"__string_0", i32 0, i32 0
  %".182" = call i32 (i8*, ...) @"printf"(i8* %".181")
  store i32 1, i32* @"judgezero"
  %".184" = load i32, i32* @"judgezero"
  ret i32 0
.156:
  br label %".147"
}

@"__string_0" = internal global [23 x i8] c"error:divisor is zero\0a\00"
define i32 @"judge"(i8 %".1")
{
__judge:
  %"c" = alloca i8
  store i8 %".1", i8* %"c"
  %".7" = load i8, i8* %"c"
  %".8" = icmp eq i8 %".7", 43
  %".9" = load i8, i8* %"c"
  %".10" = icmp eq i8 %".9", 45
  %".11" = icmp ne i1 %".8", 0
  %".12" = icmp ne i1 %".10", 0
  %".13" = or i1 %".11", %".12"
  %".14" = load i8, i8* %"c"
  %".15" = icmp eq i8 %".14", 42
  %".16" = icmp ne i1 %".13", 0
  %".17" = icmp ne i1 %".15", 0
  %".18" = or i1 %".16", %".17"
  %".19" = load i8, i8* %"c"
  %".20" = icmp eq i8 %".19", 47
  %".21" = icmp ne i1 %".18", 0
  %".22" = icmp ne i1 %".20", 0
  %".23" = or i1 %".21", %".22"
  %".24" = icmp ne i1 %".23", 0
  br i1 %".24", label %".4", label %".5"
.4:
  ret i32 1
.5:
  %".30" = load i8, i8* %"c"
  %".31" = icmp sle i8 %".30", 57
  %".32" = load i8, i8* %"c"
  %".33" = icmp sge i8 %".32", 48
  %".34" = icmp ne i1 %".31", 0
  %".35" = icmp ne i1 %".33", 0
  %".36" = and i1 %".34", %".35"
  %".37" = icmp ne i1 %".36", 0
  br i1 %".37", label %".27", label %".28"
.6:
  ret void
.27:
  ret i32 0
.28:
  %".43" = load i8, i8* %"c"
  %".44" = icmp eq i8 %".43", 91
  %".45" = icmp ne i1 %".44", 0
  br i1 %".45", label %".40", label %".41"
.29:
  br label %".6"
.40:
  ret i32 2
.41:
  %".51" = load i8, i8* %"c"
  %".52" = icmp eq i8 %".51", 93
  %".53" = icmp ne i1 %".52", 0
  br i1 %".53", label %".48", label %".49"
.42:
  br label %".29"
.48:
  ret i32 3
.49:
  %".56" = sub i32 0, 1
  ret i32 %".56"
.50:
  br label %".42"
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
  %".18" = icmp ne i8 %".17", 92
  %".19" = icmp ne i1 %".18", 0
  br i1 %".19", label %".11", label %".13"
.11:
  br label %".12"
.12:
  %".22" = load i32, i32* %"len"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* %"len"
  br label %".10"
.13:
  %"left" = alloca i32
  store i32 0, i32* %"left"
  %"pst" = alloca i32
  %".27" = sub i32 0, 2
  store i32 %".27", i32* %"pst"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 0, i32* %"i"
  %".31" = load i32, i32* %"i"
  br label %".32"
.32:
  %".37" = load i32, i32* %"i"
  %".38" = load i32, i32* %"len"
  %".39" = icmp slt i32 %".37", %".38"
  %".40" = icmp ne i1 %".39", 0
  br i1 %".40", label %".33", label %".35"
.33:
  %"jud" = alloca i32
  %".42" = load i32, i32* %"i"
  %".43" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".42"
  %".44" = load i8, i8* %".43"
  %".45" = call i32 @"judge"(i8 %".44")
  store i32 %".45", i32* %"jud"
  %".50" = load i32, i32* %"jud"
  %".51" = icmp sge i32 %".50", 0
  %".52" = icmp ne i1 %".51", 0
  br i1 %".52", label %".47", label %".48"
.34:
  %".206" = load i32, i32* %"i"
  %".207" = add i32 %".206", 1
  store i32 %".207", i32* %"i"
  %".209" = load i32, i32* %"i"
  br label %".32"
.35:
  %".213" = load i32, i32* %"left"
  %".214" = icmp ne i32 %".213", 0
  %".215" = icmp ne i1 %".214", 0
  br i1 %".215", label %".211", label %".212"
.47:
  %".57" = load i32, i32* %"i"
  %".58" = icmp ne i32 %".57", 0
  %".59" = icmp ne i1 %".58", 0
  br i1 %".59", label %".54", label %".55"
.48:
  %".202" = getelementptr inbounds [24 x i8], [24 x i8]* @"__string_9", i32 0, i32 0
  %".203" = call i32 (i8*, ...) @"printf"(i8* %".202")
  ret i32 0
.49:
  br label %".34"
.54:
  %".64" = load i32, i32* %"pst"
  %".65" = icmp eq i32 %".64", 1
  %".66" = load i32, i32* %"jud"
  %".67" = icmp eq i32 %".66", 1
  %".68" = icmp ne i1 %".65", 0
  %".69" = icmp ne i1 %".67", 0
  %".70" = and i1 %".68", %".69"
  %".71" = icmp ne i1 %".70", 0
  br i1 %".71", label %".61", label %".62"
.55:
  %".145" = load i32, i32* %"jud"
  %".146" = icmp eq i32 %".145", 1
  %".147" = load i32, i32* %"jud"
  %".148" = icmp eq i32 %".147", 3
  %".149" = icmp ne i1 %".146", 0
  %".150" = icmp ne i1 %".148", 0
  %".151" = or i1 %".149", %".150"
  %".152" = icmp ne i1 %".151", 0
  br i1 %".152", label %".143", label %".144"
.56:
  %".164" = load i32, i32* %"jud"
  %".165" = icmp eq i32 %".164", 2
  %".166" = icmp ne i1 %".165", 0
  br i1 %".166", label %".161", label %".162"
.61:
  %".73" = getelementptr inbounds [30 x i8], [30 x i8]* @"__string_2", i32 0, i32 0
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73")
  ret i32 0
.62:
  %".79" = load i32, i32* %"pst"
  %".80" = icmp eq i32 %".79", 2
  %".81" = load i32, i32* %"jud"
  %".82" = icmp ne i32 %".81", 0
  %".83" = icmp ne i1 %".80", 0
  %".84" = icmp ne i1 %".82", 0
  %".85" = and i1 %".83", %".84"
  %".86" = icmp ne i1 %".85", 0
  br i1 %".86", label %".76", label %".77"
.63:
  %".139" = load i32, i32* %"jud"
  store i32 %".139", i32* %"pst"
  %".141" = load i32, i32* %"pst"
  br label %".56"
.76:
  %".88" = getelementptr inbounds [42 x i8], [42 x i8]* @"__string_3", i32 0, i32 0
  %".89" = call i32 (i8*, ...) @"printf"(i8* %".88")
  ret i32 0
.77:
  %".94" = load i32, i32* %"pst"
  %".95" = icmp eq i32 %".94", 3
  %".96" = load i32, i32* %"jud"
  %".97" = icmp eq i32 %".96", 0
  %".98" = icmp ne i1 %".95", 0
  %".99" = icmp ne i1 %".97", 0
  %".100" = and i1 %".98", %".99"
  %".101" = icmp ne i1 %".100", 0
  br i1 %".101", label %".91", label %".92"
.78:
  br label %".63"
.91:
  %".103" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_4", i32 0, i32 0
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103")
  ret i32 0
.92:
  %".109" = load i32, i32* %"pst"
  %".110" = icmp eq i32 %".109", 0
  %".111" = load i32, i32* %"jud"
  %".112" = icmp eq i32 %".111", 2
  %".113" = icmp ne i1 %".110", 0
  %".114" = icmp ne i1 %".112", 0
  %".115" = and i1 %".113", %".114"
  %".116" = icmp ne i1 %".115", 0
  br i1 %".116", label %".106", label %".107"
.93:
  br label %".78"
.106:
  %".118" = getelementptr inbounds [39 x i8], [39 x i8]* @"__string_5", i32 0, i32 0
  %".119" = call i32 (i8*, ...) @"printf"(i8* %".118")
  ret i32 0
.107:
  %".123" = load i32, i32* %"pst"
  %".124" = icmp ne i32 %".123", 0
  %".125" = load i32, i32* %"jud"
  %".126" = icmp eq i32 %".125", 3
  %".127" = icmp ne i1 %".124", 0
  %".128" = icmp ne i1 %".126", 0
  %".129" = and i1 %".127", %".128"
  %".130" = icmp ne i1 %".129", 0
  br i1 %".130", label %".121", label %".122"
.108:
  br label %".93"
.121:
  %".132" = getelementptr inbounds [36 x i8], [36 x i8]* @"__string_6", i32 0, i32 0
  %".133" = call i32 (i8*, ...) @"printf"(i8* %".132")
  ret i32 0
.122:
  br label %".108"
.143:
  %".154" = getelementptr inbounds [49 x i8], [49 x i8]* @"__string_7", i32 0, i32 0
  %".155" = call i32 (i8*, ...) @"printf"(i8* %".154")
  ret i32 0
.144:
  %".157" = load i32, i32* %"jud"
  store i32 %".157", i32* %"pst"
  %".159" = load i32, i32* %"pst"
  br label %".56"
.161:
  %".168" = load i32, i32* %"left"
  %".169" = add i32 %".168", 1
  store i32 %".169", i32* %"left"
  %".171" = load i32, i32* %"left"
  br label %".163"
.162:
  %".175" = load i32, i32* %"jud"
  %".176" = icmp eq i32 %".175", 3
  %".177" = icmp ne i1 %".176", 0
  br i1 %".177", label %".173", label %".174"
.163:
  %".185" = load i32, i32* %"i"
  %".186" = getelementptr inbounds [100 x i8], [100 x i8]* @"strs", i32 0, i32 %".185"
  %".187" = load i32, i32* %"i"
  %".188" = getelementptr inbounds [100 x i8], [100 x i8]* @"stringone", i32 0, i32 %".187"
  %".189" = load i8, i8* %".188"
  store i8 %".189", i8* %".186"
  %".191" = load i8, i8* %".186"
  %".194" = load i32, i32* %"left"
  %".195" = icmp slt i32 %".194", 0
  %".196" = icmp ne i1 %".195", 0
  br i1 %".196", label %".192", label %".193"
.173:
  %".179" = load i32, i32* %"left"
  %".180" = sub i32 %".179", 1
  store i32 %".180", i32* %"left"
  %".182" = load i32, i32* %"left"
  br label %".174"
.174:
  br label %".163"
.192:
  %".198" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_8", i32 0, i32 0
  %".199" = call i32 (i8*, ...) @"printf"(i8* %".198")
  ret i32 0
.193:
  br label %".49"
.211:
  %".217" = getelementptr inbounds [20 x i8], [20 x i8]* @"__string_10", i32 0, i32 0
  %".218" = call i32 (i8*, ...) @"printf"(i8* %".217")
  ret i32 0
.212:
  call void @"Polish"()
  %"num" = alloca i32
  %".221" = call i32 @"cal"()
  store i32 %".221", i32* %"num"
  %".225" = load i32, i32* @"judgezero"
  %".226" = icmp eq i32 %".225", 1
  %".227" = icmp ne i1 %".226", 0
  br i1 %".227", label %".223", label %".224"
.223:
  ret i32 0
.224:
  %".230" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_11", i32 0, i32 0
  %".231" = load i32, i32* %"num"
  %".232" = call i32 (i8*, ...) @"printf"(i8* %".230", i32 %".231")
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
@"__string_11" = internal global [4 x i8] c"%d\0a\00"