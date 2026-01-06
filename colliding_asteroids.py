def collidingAsteroids(asteroids):
    if len(asteroids) < 2:
        return asteroids
    i = 0
    while i < len(asteroids): 
        current = asteroids[i]
        if current > 0:
            if i + 1 == len(asteroids):
                i += 1
                continue
            next = asteroids[i + 1]
            if next > 0:
                i += 1
                continue
            collision = current + next
            if collision == 0:
                del asteroids[i + 1]
                del asteroids[i]
                continue
            elif collision > 0:
                del asteroids[i + 1]
                i += 1
            else:
                del asteroids[i]
        else:
            if i - 1 < 0:
                i += 1
                continue
            left = asteroids[i - 1]
            if left < 0:
                i += 1
                continue
            collision = current + left
            if collision == 0:
                del asteroids[i]
                del asteroids[i - 1]
                continue
            elif collision < 0:
                del asteroids[i - 1]
                i -= 1
                continue
            else:
                del asteroids[i]
    return asteroids 
        
