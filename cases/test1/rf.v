module top(in, x, y, out, out2);
input in, x, y;
output out, out2;

and a(out2, x, y);
and c(out, in, x);

endmodule