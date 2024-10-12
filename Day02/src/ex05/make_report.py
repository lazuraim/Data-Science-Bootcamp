import analytics as an
import config as conf

if __name__ == "__main__":
     try:
          r1 = an.Research(conf.filepath)
          file_content = r1.file_reader()

          c1 = r1.calc
          h, t = c1.counts(file_content)
          h_per, t_per = c1.fractions()

          a1 = an.Analytics()
          c_heads, c_tails = a1.count_in_prediction(a1.predict_random(conf.num_of_steps))
          data = conf.template.format(total = h + t, tails = t, heads = h, \
               tail_percent = t_per, head_percent = h_per, steps = conf.num_of_steps, count_tails = c_tails, count_heads = c_heads)
          a1.save_file(data, 'report', 'txt')
     except Exception as error_message:
          print(error_message)

