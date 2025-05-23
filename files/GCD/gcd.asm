gcd:
        mov     eax, edi
repeat:
        test    esi, esi
        je      finish
        cdq
        idiv    esi
        mov     eax, esi
        mov     esi, edx
        jmp     repeat
finish:
        ret
