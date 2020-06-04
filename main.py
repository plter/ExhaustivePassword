words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+=.;:?'


def crack_with_depth(depth):
    def crack(prefix, current_depth):
        if current_depth <= depth:
            for w in words:
                key = prefix + w
                print(key)
                crack(key, current_depth + 1)

    crack('', 1)


crack_with_depth(6)
