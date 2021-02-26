module top(in, x, y, out, out2);
input in, x, y;
output out, out2;

or  a(out2, x, y);
and b(out, in, x);

endmodule