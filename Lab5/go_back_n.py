import random
import time

def go_back_n(total_frames=10, window_size=4, loss_probability=0.3):
    base = 0
    next_frame = 0

    while base < total_frames:
        print(f"\nWindow: {base} to {min(base + window_size - 1, total_frames - 1)}")

        for i in range(base, min(base + window_size, total_frames)):
            print(f" Sending Frame {i}")
            next_frame += 1

        lost_frame = None
        for i in range(base, min(base + window_size, total_frames)):
            if random.random() < loss_probability:
                lost_frame = i
                print(f" Frame {i} lost! → Go-Back-N triggered")
                break
            else:
                print(f" ACK {i} received")

        if lost_frame is not None:
            print(f" Retransmitting from Frame {lost_frame}...")
            next_frame = lost_frame
            time.sleep(1)
        else:
            base += window_size
            time.sleep(0.5)

if __name__ == "__main__":
    print("=== Go-Back-N ARQ Simulation ===")
    go_back_n(total_frames=12, window_size=4, loss_probability=0.3)
