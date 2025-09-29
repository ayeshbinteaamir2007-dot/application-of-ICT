section .data
    msg_add db "Addition Result: ",0
    len_add equ $-msg_add
    msg_mul db "Multiplication Result: ",0
    len_mul equ $-msg_mul
    newline db 10

section .bss
    res_str resb 16         ; buffer for number string

section .text
    global _start

_start:
    ; Hardcoded numbers
    mov eax, 5              ; first number
    mov ebx, 3              ; second number

    ; ----- Addition -----
    add eax, ebx            ; eax = 5 + 3
    mov esi, eax            ; save result

    ; print message
    mov eax, 4
    mov ebx, 1
    mov ecx, msg_add
    mov edx, len_add
    int 0x80

    ; print result
    mov eax, esi
    call print_num
    call print_newline

    ; ----- Multiplication -----
    mov eax, 5
    mov ebx, 3
    imul eax, ebx           ; eax = 5 * 3
    mov esi, eax

    ; print message
    mov eax, 4
    mov ebx, 1
    mov ecx, msg_mul
    mov edx, len_mul
    int 0x80

    ; print result
    mov eax, esi
    call print_num
    call print_newline

    ; exit
    mov eax, 1
    xor ebx, ebx
    int 0x80


; ----------------------------------
; print_num: print integer in eax
; ----------------------------------
print_num:
    lea edi, [res_str+15]   ; point to end of buffer
    mov byte [edi], 0
    mov ebx, 10

.convert_loop:
    dec edi
    xor edx, edx
    div ebx                 ; eax / 10 → eax, remainder → edx
    add dl, '0'
    mov [edi], dl
    test eax, eax
    jnz .convert_loop

    ; length = (res_str+15) - edi
    lea eax, [res_str+15]
    sub eax, edi
    mov edx, eax            ; length

    mov ecx, edi            ; string start
    mov ebx, 1              ; stdout
    mov eax, 4              ; sys_write
    int 0x80
    ret

print_newline:
    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 1
    int 0x80
    ret
