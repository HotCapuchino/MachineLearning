
from TF_IDF.tf_idf import TF_IDF


def divide_text(chapters_names: list, text: str) -> list:
    chapters = []
    for i in range(len(chapters_names) - 1):
        this_chap = chapters_names[i]
        next_chap = chapters_names[i + 1]
        chapter_start = text.find(this_chap)
        chapter_end = text.find(next_chap)
        if chapter_start >= 0 and chapter_end >= 0:
            chapters.append(text[chapter_start:chapter_end])
    return chapters

def get_chapters(text: str) -> tuple:
    chaps_names = []
    chaps, story = text.split('DIVIDER:')
    for row in chaps.split('\n'):
        if not row == '' and 'CHAPTER' in row:
            chap = row.split('—')[0].upper()
            chaps_names.append(chap)
    return divide_text(chaps_names, story), chaps_names


if __name__ == '__main__':
    WORDS_AMOUNT = 10

    document = open('./res/moby-dick.txt')
    chapters, chaps_names = get_chapters(document.read())
    document.close()

    tf_idf = TF_IDF(chapters)
    tf_idf.calculate_tf_idf()

    out = open('./out/tf_idf_moby-dick.txt', 'w')
    for index, chap in enumerate(chapters):
        out.write(f'Top {WORDS_AMOUNT} words for {chaps_names[index]}:\n')
        top_words = tf_idf.get_top_words(index, WORDS_AMOUNT)
        for word_index, word in enumerate(top_words):
            out.write(f'{word_index + 1}. {word}\n')
        out.write('\n')
    out.close