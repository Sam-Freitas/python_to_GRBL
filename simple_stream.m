% this is a simple gcode sender for matlab
% Samuel Freitas 5/31/2022

clear all
close all force hidden

GRBL_port_path = "COM4";
gcode_path = "grbl_test.gcode";
BAUD_RATE = 115200;

gcode = importdata(gcode_path);
gcode_string = string(gcode);

ser = serialport(GRBL_port_path,BAUD_RATE);
ser.Timeout = 0.1;

send_wake_up(ser)

for i = 1:length(gcode_string)
    
    this_string = gcode_string(i);
    cleaned_line = char(remove_eol_chars(remove_comment(this_string)));
    
    if ~(isempty(cleaned_line))
        
        disp(string(cleaned_line))
        
        writeline(ser,cleaned_line);
        wait_for_movement_completion(ser,cleaned_line);
        
        this_decoded_string = decode_unicode(cleaned_line);
        
        disp(this_string);
        disp(num2str(cleaned_line));
        disp(this_decoded_string);
        disp(char(13))
        
    end
end


function out = remove_comment(this_string)
    comment_idx = find(char(this_string) == ';', 1);
    if isempty(comment_idx)
        out = this_string;
    else
        temp = char(this_string);
        out = string(temp(1:comment_idx-1));
    end
end

function send_wake_up(ser)
%     # Wake up
%     # Hit enter a few times to wake the Printrbot
    writeline(ser, char("\r\n\r\n"))
    pause(2)  % Wait for Printrbot to initialize
    flush(ser,"input")  % Flush startup text in serial input

end

function out = encode_string(in_string)
% found that you just need to send chars to the GRBL controller as a line
    out = double(char(in_string));
end

function out = decode_unicode(in_unicode)
    out = string(char(in_unicode));
end

function out = remove_eol_chars(in_string)
    out = strip(in_string);
end

function wait_for_movement_completion(ser,cleaned_line)

    pause(1)
    
    if ~isequal(cleaned_line,'$X') && ~isequal(cleaned_line,'$$')
        
        idle_counter = 0;

        while 1

%             # Event().wait(0.01)
            flush(ser,"input")
            command = char(['?\n']);
            writeline(ser,command)
            grbl_out = readline(ser);
            grbl_response = decode_unicode(strip(grbl_out));

            if ~isequal(grbl_response,'ok')

                if contains(grbl_response,'Idle')
                    idle_counter = idle_counter + 1;
                end
            end

            if idle_counter > 10
                break
            end
        end
        
    end

end







