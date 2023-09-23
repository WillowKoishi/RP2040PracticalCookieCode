import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

# This is from the base kmk boot.py
supervisor.set_next_stack_limit(4096 + 4096)


row = digitalio.DigitalInOut(board.GP15)

row.switch_to_input(pull=digitalio.Pull.UP)

if row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()
