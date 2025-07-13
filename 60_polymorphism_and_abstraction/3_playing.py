def start_playing(some_instance):
    return some_instance.play()


class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))