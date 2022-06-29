f = open("./uvm_virtual_sequencer_codes/virtual_sequencer.sv", "w")

f.write('// Virtual Sequencer Class\n')
f.write('class virtual_seqr extend uvm_sequencer;\n')
f.write(' `uvm_component_utils(virtual_seqr)\n')
f.write('\n')
f.write(' // Target Sequencer Handles\n')
f.write('  ahb_seqr SQR_AHB;\n')
f.write('  axi_seqr SQR_AXI;\n')
f.write('\n')
f.write(' // Constructor\n')
f.write(' function new (string name = "virtual_seqr", uvm_component parent);\n')
f.write('  super.new(name, parent);\n')
f.write(' endfunction: new\n')
f.write('\n')
f.write('endclass: virtual_seqr\n')

f.close()

#open and read the file after the appending:
f = open("./uvm_virtual_sequencer_codes/virtual_sequencer.sv", "r")
print(f.read())