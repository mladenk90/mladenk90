#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int main(void)
{
    string text = get_string("Text: ");

    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
// for spaces
        else if (text[i] == ' ')
        {
            words++;
        }
// for . ! ?
        else if (text[i] == '.' || text[i] == '!'  || text[i] == '?')
        {
            sentences++;
        }
    }

    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);
// before 1
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
// higher than 16
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
// anything in between
    else
    {
        printf("Grade %i\n", index);
    }
}