library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.math_real.all;

entity shift_reg_tb is 
end shift_reg_tb;

architecture beh of shift_reg_tb is
component shift_reg_4bit is
    port(
        D: in std_logic;
        clk: in std_logic;
        Q: out std_logic_vector(3 downto 0)
    );
    end component;
    signal D_tb, clk: STD_LOGIC;
    signal Q_tb : STD_LOGIC_VECTOR(3 downto 0);
    
        
begin
    DUT: shift_reg_4bit
     port map(
        D => D_tb,
        clk => clk,
        Q => Q_tb
    );


    stim:process 
    begin
        
        
    end process;

end architecture;