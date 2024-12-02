from collections import defaultdict

def find_the_longest(fragments):
    start_dict = defaultdict(list)
    end_dict = defaultdict(list)

    for fragment in fragments:
        start_dict[fragment[:2]].append(fragment)
        end_dict[fragment[-2:]].append(fragment)

    def line_sequence(fragment, used_fragments):
        sequence = fragment
        used_fragments.add(fragment)

        while True:
            tail = sequence[-2:]
            next_fragments = start_dict[tail]
            next_fragment = next(
                (f for f in next_fragments if f not in used_fragments), None
            )
            if not next_fragment:
                break
            sequence += next_fragment[2:]
            used_fragments.add(next_fragment)

        while True:
            head = sequence[:2]
            prev_fragments = end_dict[head]
            prev_fragment = next(
                (f for f in prev_fragments if f not in used_fragments), None
            )
            if not prev_fragment:
                break
            sequence = prev_fragment[:-2] + sequence
            used_fragments.add(prev_fragment)

        return sequence

    longest = ""
    for fragment in fragments:
        used_fragments = set()
        sequence = line_sequence(fragment, used_fragments)
        if len(sequence) > len(longest):
            longest = sequence

    return longest

if __name__ == "__main__":
    file_path = r"Вставте абсолютний шлях до файлу" 
    
    try:
        with open(file_path, 'r') as file:
            fragments = file.read().splitlines()
            fragments = [frag.strip() for frag in fragments if frag.strip().isdigit()]
        
        longest_sequence = find_the_longest(fragments)
        print("Найдовша послідовність:", longest_sequence)
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print("Сталася помилка:", str(e))
