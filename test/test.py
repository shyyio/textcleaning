from unittest import TestCase

from textcleaning import preprocess


class TestText(TestCase):

    def test_html_invalid(self):
        text = ""
        cleaned = preprocess(
            text,
            clean_html=True,
        )
        expected = ""

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_1(self):
        text = "<div>Hello, <strong>world</strong></div>"
        cleaned = preprocess(
            text,
            clean_html=True,
        )
        expected = "Hello, world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_2(self):
        text = "<div>Hello, <strong>world</strong></div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True
        )
        expected = "hello, world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_4(self):
        text = "<div>\n Hello, \t\n<strong> world    </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
        )
        expected = "hello, world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_5(self):
        text = "<div>\n Hello, \t\n<strong> world    </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True
        )
        expected = "hello world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_6(self):
        text = "<div>\n Hello, \t\n<strong>a the world    </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords_en=True
        )
        expected = "hello world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_7(self):
        text = "<div>\n Hello, \t\n<strong>a the worlds    </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords_en=True,
            lemmatize=True
        )
        expected = "hello world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_8(self):
        text = "<div>\n Hello, \t\n<strong>a the worlds!    </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            remove_stopwords_en=True,
            lemmatize=True
        )
        expected = "hello world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_9(self):
        text = "<div>\n Hello, \t\n<strong>world! it's it`s   </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=True,
            fix_single_quotes=True
        )
        expected = "hello world it's it's"

        self.assertEqual(" ".join(cleaned), expected)
    
    def test_single_quote(self):
        text = "it's it`s it’s"
        cleaned = preprocess(
            text,
            lowercase=True,
            fix_single_quotes=True
        )
        expected = "it's it's it's"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_10(self):
        text = "<div>\n Hello, \t\n<strong>world! it's it`s https://google.ca/test/abc.pdf  </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=True,
            fix_single_quotes=True,
            remove_urls=True
        )
        expected = "hello world it's it's"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_11(self):
        text = "<div>\n Hello, \t\n<strong>world! it's it`s & | </strong>\n\t</div>"
        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=True,
            fix_single_quotes=True,
            remove_stopwords_en=True,
            remove_urls=True
        )
        expected = "hello world |"

        self.assertEqual(" ".join(cleaned), expected)

    def test_html_no_root(self):
        text = "<a href=\"#p217709510\" class=\"quotelink\">&gt;&gt;217709510</a><br>Is there a<wbr>servant that is against civilization and humanity?<br>Literally instant summon."

        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=False,
            fix_single_quotes=True,
            remove_stopwords_en=False,
            remove_urls=False
        )

        expected = ">>217709510 is there a servant that is against civilization and humanity literally instant summon"
        self.assertEqual(" ".join(cleaned), expected)

    def test_html_entity(self):
        text = "doesn&#039;t"

        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=False,
            fix_single_quotes=True,
            remove_stopwords_en=False,
            remove_urls=False
        )

        expected = "doesn't"
        self.assertEqual(" ".join(cleaned), expected)

    def test_html_invalid_attribute(self):
        text = '<root><iframe width="560" height="315" src=" " title="youtube video player" frameborder="0" allowfullscreen></iframe></root>'

        cleaned = preprocess(
            text,
            clean_html=True,
            lowercase=True,
            remove_punctuation=True,
            lemmatize=False,
            fix_single_quotes=True,
            remove_stopwords_en=False,
            remove_urls=False
        )

        expected = ""

        self.assertEqual(" ".join(cleaned), expected)

    def test_bigrams(self):
        text = "x A b c d e f g h"
        cleaned = preprocess(
            text,
            lowercase=True,
            bigrams={
                ("a", "b"),
                ("c", "d"),
                ("f", "g"),
            }
        )
        expected = "x a_b c_d e f_g h"

        self.assertEqual(" ".join(cleaned), expected)

    def test_trigrams(self):
        text = "x A b c d e f g h"
        cleaned = preprocess(
            text,
            lowercase=True,
            trigrams={
                ("a", "b", "c"),
                ("e", "f", "g"),
            }
        )
        expected = "x a_b_c d e_f_g h"

        self.assertEqual(" ".join(cleaned), expected)

    def test_remove_numbers(self):
        text = "Hello1 test1124test 12 1 1111111 world"
        cleaned = preprocess(
            text,
            lowercase=True,
            remove_numbers=True
        )
        expected = "hello1 test1124test world"

        self.assertEqual(" ".join(cleaned), expected)

    def test_strip_quotes(self):
        text = "'hi' “test” 'hello\""
        cleaned = preprocess(
            text,
            strip_quotes=True
        )
        expected = "hi test hello"

        self.assertEqual(" ".join(cleaned), expected)

    def test_strip_dashes(self):
        text = "yes -But something-something -- hello aa--bb"
        cleaned = preprocess(
            text,
            strip_dashes=True
        )
        expected = "yes But something-something hello aa-bb"

        self.assertEqual(" ".join(cleaned), expected)

    def test_word_tokenize(self):
        text = "i cannot believe'"
        cleaned = preprocess(
            text,
            use_nltk_tokenizer=True
        )
        expected = "i can not believe '"

        self.assertEqual(" ".join(cleaned), expected)
        
    def test_fix_double_quotes(self):
        text = "a «b» “c”"
        cleaned = preprocess(
            text,
            fix_double_quotes=True
        )
        expected = "a \"b\" \"c\""

        self.assertEqual(" ".join(cleaned), expected)

    def test_unidecode(self):
        
        self.assertEqual(
            " ".join(preprocess("𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )

        self.assertEqual(
            " ".join(preprocess("𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )
        
        self.assertEqual(
            " ".join(preprocess("𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )

        self.assertEqual(
            " ".join(preprocess("𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )

        self.assertEqual(
            " ".join(preprocess("𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )

        self.assertEqual(
            " ".join(preprocess("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", asciifold=True)),
            "abcdefghijklmnopqrstuvwxyz"
        )
    
    def test_demojize(self):
        self.assertEqual(
            " ".join(preprocess("test️ ❤️", demojize=True)),
            "test :red_heart:"
        )
        
        self.assertEqual(
            " ".join(preprocess("test️ ❤️ 𝕒𝕓𝕔", demojize=True, asciifold=True)),
            "test :red_heart: abc"
        )

    def test_asciifold_accents(self):
        self.assertEqual(
            " ".join(preprocess("ç â ä à é ê ë è ï î ì ô ö ò ú ü û ù ÿ", asciifold=True)),
            "c a a a e e e e i i i o o o u u u u y"
        )


    def test_normalize_single_quotes(self):
        self.assertEqual(
            " ".join(preprocess("what's that? 'woman' test' '' 'yeah 'test-test'", normalize_single_quotes=True)),
            "what's that? \"woman\" test' '' 'yeah \"test-test\""
        )
