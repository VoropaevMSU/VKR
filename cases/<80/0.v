// Benchmark "dsd" written by ABC on Sat Apr 24 22:01:03 2021module dsd (     a, b, c, d,    F  );  input  a, b, c, d;  output F;  wire new_n6_, new_n7_, new_n8_, new_n9_, new_n10_, new_n11_, new_n12_,    new_n13_, new_n14_, new_n15_, new_n16_, new_n17_, new_n18_, new_n19_,    new_n20_, new_n21_, new_n22_, new_n23_, new_n24_, new_n25_, new_n26_,    new_n27_, new_n28_, new_n29_, new_n30_, new_n31_, new_n32_, new_n33_,    new_n34_, new_n35_, new_n36_, new_n37_, new_n11_1, new_n7_1, new_n12_1, new_n19_1, new_n27_1, new_n17_1, new_n18_1, new_n15_1, c1, new_n26_1, new_n16_1, new_n28_1, d1, new_n10_1, new_n13_1, new_n24_1, new_n23_1, new_n20_1, new_n21_1, a1, b1, new_n9_1, new_n6_1, new_n29_1, new_n25_1, new_n8_1, new_n14_1, new_n22_1;not b(a1, a);
nor a(new_n6_, a1, b);
not b(b1, b);
nand a(new_n7_, a, b1);
not b(new_n6_1, new_n6_);
not b(new_n7_1, new_n7_);
_DC a(new_n8_, new_n6_1, new_n7_1);
nor a(new_n9_, a, b);
not b(a1, a);
not b(b1, b);
xor a(new_n10_, a1, b1);
not b(new_n9_1, new_n9_);
not b(new_n10_1, new_n10_);
_DC a(new_n11_, new_n9_1, new_n10_1);
not b(c1, c);
nor a(new_n12_, c1, d);
not b(d1, d);
nor a(new_n13_, c, d1);
not b(new_n12_1, new_n12_);
not b(new_n13_1, new_n13_);
nor a(new_n14_, new_n12_1, new_n13_1);
xor a(new_n15_, c, d);
not b(c1, c);
not b(d1, d);
and a(new_n16_, c1, d1);
not b(new_n15_1, new_n15_);
not b(new_n16_1, new_n16_);
nand a(new_n17_, new_n15_1, new_n16_1);
nor a(new_n18_, c, new_n8_);
not b(c1, c);
not b(new_n8_1, new_n8_);
nand a(new_n19_, c1, new_n8_1);
not b(new_n18_1, new_n18_);
not b(new_n19_1, new_n19_);
or a(new_n20_, new_n18_1, new_n19_1);
nor a(new_n21_, d, new_n20_);
not b(d1, d);
not b(new_n20_1, new_n20_);
xor a(new_n22_, d1, new_n20_1);
not b(new_n21_1, new_n21_);
not b(new_n22_1, new_n22_);
nand a(new_n23_, new_n21_1, new_n22_1);
not b(c1, c);
xor a(new_n24_, c1, new_n11_);
not b(new_n11_1, new_n11_);
or a(new_n25_, c, new_n11_1);
not b(new_n24_1, new_n24_);
not b(new_n25_1, new_n25_);
and a(new_n26_, new_n24_1, new_n25_1);
and a(new_n27_, d, new_n26_);
not b(d1, d);
not b(new_n26_1, new_n26_);
nor a(new_n28_, d1, new_n26_1);
not b(new_n27_1, new_n27_);
not b(new_n28_1, new_n28_);
nand a(new_n29_, new_n27_1, new_n28_1);
not b(new_n8_1, new_n8_);
not b(new_n11_1, new_n11_);
_DC a(new_n30_, new_n8_1, new_n11_1);
not b(new_n11_1, new_n11_);
nor a(new_n31_, new_n11_1, new_n30_);
not b(new_n8_1, new_n8_);
or a(new_n32_, new_n8_1, new_n31_);
not b(new_n14_1, new_n14_);
or a(new_n33_, new_n14_1, new_n32_);
not b(new_n17_1, new_n17_);
xor a(new_n34_, new_n17_1, new_n33_);
not b(new_n17_1, new_n17_);
_DC a(new_n35_, new_n17_1, new_n34_);
not b(new_n14_1, new_n14_);
nor a(new_n36_, new_n14_1, new_n35_);
not b(new_n23_1, new_n23_);
xor a(new_n37_, new_n23_1, new_n36_);
not b(new_n29_1, new_n29_);
xor a(F, new_n29_1, new_n37_);
endmodule;