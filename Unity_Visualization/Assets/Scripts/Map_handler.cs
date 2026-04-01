using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
 using UnityEngine.UI;

public class Map_handler : MonoBehaviour
{
    public world_data world_Data = new world_data();

    public turns_data turns_data = new turns_data();

    public bool play_pause_flag;
    bool changed;

    [Header("Buttons")]
    public Button play_pause;
    public Button next_turn;
    public Button previous_turn;

    // Sprites do fundo do Hexagono
    [Header("Sprites")]

    public Sprite sprite_pause;
    public Sprite sprite_play;

    // GameObject dos paises
    [Header("GameObject Countries")]
    public GameObject GameObject_Brasil_country;
    public GameObject GameObject_Peru_country;
    public GameObject GameObject_Argentina_country;
    public GameObject GameObject_Venezuela_country;

    public GameObject GameObject_Alaska_country;
    public GameObject GameObject_Northwest_America_country;
    public GameObject GameObject_Greenland_country;
    public GameObject GameObject_Ontario_country;
    public GameObject GameObject_Alberta_country;
    public GameObject GameObject_Western_America_country;
    public GameObject GameObject_Central_America_country;
    public GameObject GameObject_Eastern_America_country;
    public GameObject GameObject_Quebec_country;

    public GameObject GameObject_Skandinavia_country;
    public GameObject GameObject_Western_Europe_country;
    public GameObject GameObject_Iceland_country;
    public GameObject GameObject_Great_Britain_country;
    public GameObject GameObject_Southern_Europe_country;
    public GameObject GameObject_Northern_Europe_country;
    public GameObject GameObject_Ukraine_country;

    public GameObject GameObject_North_Africa_country;
    public GameObject GameObject_Egypt_country;
    public GameObject GameObject_East_Africa_country;
    public GameObject GameObject_Congo_country;
    public GameObject GameObject_South_Africa_country;
    public GameObject GameObject_Madagascar_country;

    public GameObject GameObject_Ural_country;
    public GameObject GameObject_Siberia_country;
    public GameObject GameObject_Yakutsk_country;
    public GameObject GameObject_Irkutsk_country;
    public GameObject GameObject_Kamchatka_country;
    public GameObject GameObject_Mongolia_country;
    public GameObject GameObject_China_country;
    public GameObject GameObject_Afganistan_country;
    public GameObject GameObject_India_country;
    public GameObject GameObject_Siam_country;
    public GameObject GameObject_Middle_East_country;
    public GameObject GameObject_Japan_country;

    public GameObject GameObject_Eastern_Australia_country;
    public GameObject GameObject_Western_Australia_country;
    public GameObject GameObject_Indoneasia_country;
    public GameObject GameObject_Papua_New_Guinea_country;

    Dictionary<string, country> countries;

    public Slider turns_slider;

    public Slider commands_slider;

    [Header("Colors")]
    public Color32 Player_1_Color;
    public Color32 Player_2_Color;


    private IEnumerator coroutine;

    
    public void make_dict_turn_data(int selected_turn)
    {
        //Debug.Log("entrou - Turns");
        foreach (KeyValuePair<string,country> c in countries)
        {
            c.Value.owner = c.Value.owner_first;
            c.Value.n_troops = c.Value.n_troops_first;
        }

        for(int i = 0; i<selected_turn; i++)
        {
            for(int y = 0; y<turns_data.turns[i].calls.Length; y++)
            {
                if(turns_data.turns[i].calls[y].tipo == "set_new_troops")
                {
                    countries[turns_data.turns[i].calls[y].name_in].n_troops += turns_data.turns[i].calls[y].in_number;
                }
                else if(turns_data.turns[i].calls[y].tipo == "attack")
                {
                    countries[turns_data.turns[i].calls[y].name_out].n_troops -= turns_data.turns[i].calls[y].out_number;

                    countries[turns_data.turns[i].calls[y].name_in].n_troops -= turns_data.turns[i].calls[y].in_number;

                    if(turns_data.turns[i].calls[y].conquered == true)
                    {
                        countries[turns_data.turns[i].calls[y].name_in].n_troops += (turns_data.turns[i].calls[y].dice_number - turns_data.turns[i].calls[y].out_number);
                        countries[turns_data.turns[i].calls[y].name_out].n_troops -= turns_data.turns[i].calls[y].dice_number;
                        if(countries[turns_data.turns[i].calls[y].name_in].owner == 1)
                        {
                            countries[turns_data.turns[i].calls[y].name_in].owner = 2;
                        }
                        else
                        {
                            countries[turns_data.turns[i].calls[y].name_in].owner = 1;
                        }
                    }
                }
                else if(turns_data.turns[i].calls[y].tipo == "move_troops")
                {
                    countries[turns_data.turns[i].calls[y].name_out].n_troops -= turns_data.turns[i].calls[y].out_number;

                    countries[turns_data.turns[i].calls[y].name_in].n_troops += turns_data.turns[i].calls[y].in_number;
                }

            }
        }

        foreach (KeyValuePair<string,country> c in countries)
        {
            c.Value.owner_first_command = c.Value.owner;
            c.Value.n_troops_first_command = c.Value.n_troops;
        }
        
    }

    public void make_dict_command_data(int selected_turn, int selected_command)
    {
        //Debug.Log("entrou - Commands");
        foreach (KeyValuePair<string,country> c in countries)
        {
            c.Value.owner = c.Value.owner_first_command;
            c.Value.n_troops = c.Value.n_troops_first_command;
        }

        for(int y = 0; y<selected_command; y++)
        {
            if(turns_data.turns[selected_turn].calls[y].tipo == "set_new_troops")
            {
                //Debug.Log("set_new_troops");
                countries[turns_data.turns[selected_turn].calls[y].name_in].n_troops += turns_data.turns[selected_turn].calls[y].in_number;
            }
            else if(turns_data.turns[selected_turn].calls[y].tipo == "attack")
            {
                //Debug.Log("attack");
                countries[turns_data.turns[selected_turn].calls[y].name_out].n_troops -= turns_data.turns[selected_turn].calls[y].out_number;

                countries[turns_data.turns[selected_turn].calls[y].name_in].n_troops -= turns_data.turns[selected_turn].calls[y].in_number;

                if(turns_data.turns[selected_turn].calls[y].conquered == true)
                {
                    countries[turns_data.turns[selected_turn].calls[y].name_in].n_troops += (turns_data.turns[selected_turn].calls[y].dice_number - turns_data.turns[selected_turn].calls[y].out_number);
                    countries[turns_data.turns[selected_turn].calls[y].name_out].n_troops -= turns_data.turns[selected_turn].calls[y].dice_number;
                    if(countries[turns_data.turns[selected_turn].calls[y].name_in].owner == 1)
                    {
                        countries[turns_data.turns[selected_turn].calls[y].name_in].owner = 2;
                    }
                    else
                    {
                        countries[turns_data.turns[selected_turn].calls[y].name_in].owner = 1;
                    }
                }
            }
            else if(turns_data.turns[selected_turn].calls[y].tipo == "move_troops")
            {
                //Debug.Log("move_troops");
                countries[turns_data.turns[selected_turn].calls[y].name_out].n_troops -= turns_data.turns[selected_turn].calls[y].out_number;

                countries[turns_data.turns[selected_turn].calls[y].name_in].n_troops += turns_data.turns[selected_turn].calls[y].in_number;
            }
        }
    }

    public void OnSliderValueChanged_turn(float value)
    {
        make_dict_turn_data((int)value);
        commands_slider.maxValue = turns_data.turns[(int)value].calls.Length-1;
        commands_slider.value = 0;
        make_dict_command_data((int)value, (int)commands_slider.value);
    }

    public void OnSliderValueChanged_command(float value)
    {
        make_dict_command_data((int)turns_slider.value ,(int)value);
    }

    public void OnClick_button_play_pause(){
		if (play_pause_flag == false)
        {
            play_pause.GetComponent<Image>().sprite = sprite_pause;
            play_pause_flag = true;
            //StartCoroutine(coroutine);
        }
        else
        {
            play_pause.GetComponent<Image>().sprite = sprite_play;
            play_pause_flag = false;
            //StopCoroutine(coroutine);
        }
	}

    IEnumerator commands_control()
    {
        while(true)
        {
            if( (play_pause_flag == true) && ((int)turns_slider.value <= turns_slider.maxValue) )
            {
                if(turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].tipo == "set_new_troops")
                {
                    //Debug.Log("set_new_troops");
                    countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].n_troops += turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].in_number;
                }
                else if(turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].tipo == "attack")
                {
                    //Debug.Log("attack");
                    countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_out].n_troops -= turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].out_number;

                    countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].n_troops -= turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].in_number;

                    if(turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].conquered == true)
                    {
                        countries[turns_data.turns[(int)(int)turns_slider.value].calls[(int)commands_slider.value].name_in].n_troops += (turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].dice_number - turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].out_number);
                        countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_out].n_troops -= turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].dice_number;
                        if(countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].owner == 1)
                        {
                            countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].owner = 2;
                        }
                        else
                        {
                            countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].owner = 1;
                        }
                    }
                }
                else if(turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].tipo == "move_troops")
                {
                    //Debug.Log("move_troops");
                    countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_out].n_troops -= turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].out_number;

                    countries[turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].name_in].n_troops += turns_data.turns[(int)turns_slider.value].calls[(int)commands_slider.value].in_number;
                }
                //yield return new WaitForSeconds(10f);

                if((int)commands_slider.value < (int)commands_slider.maxValue)
                {
                    Debug.Log("aumentou o comando");
                    commands_slider.value += 1;
                }
                else if((int)commands_slider.value == (int)commands_slider.maxValue)
                {
                    if(turns_slider.value < turns_slider.maxValue)
                    {
                        Debug.Log("aumentou o turno");
                        turns_slider.value += 1;
                    }
                    else
                    {
                        Debug.Log("parou");
                        OnClick_button_play_pause();
                    }
                    
                    //commands_slider.maxValue = turns_data.turns[(int)turns_slider.value].calls.Length;
                    //commands_slider.value = 0;
                }
                
            }
            yield return new WaitForSeconds(1f);
        }
    }

    /*if(turns_slider.value == turns_slider.maxValue-1)
    {
        OnClick_button_play_pause();
        Debug.Log("tttttt");
        turns_slider.value += 1;
        commands_slider.maxValue = turns_data.turns[(int)turns_slider.value].calls.Length;
        commands_slider.value = 0;
    }
    else if(turns_slider.value < turns_slider.maxValue)
    {
        Debug.Log("ttttttttttttttttt");
        turns_slider.value += 1;
        commands_slider.maxValue = turns_data.turns[(int)turns_slider.value].calls.Length;
        commands_slider.value = 0;
    }*/

    void Start()
    {
        play_pause_flag = false;

        coroutine = commands_control();

        StartCoroutine(coroutine);

        turns_data = gameObject.GetComponent<reader>().turns_data;

        world_Data = gameObject.GetComponent<reader>().world_Data;

        //Debug.Log(turns_data.turns.Length);

        turns_slider.maxValue = turns_data.turns.Length-1;
        commands_slider.maxValue = turns_data.turns[0].calls.Length-1;

        countries = new Dictionary<string, country>();

        for(int i = 0; i<world_Data.countries.Length; i++)
        {
            world_Data.countries[i].owner_first = world_Data.countries[i].owner;
            world_Data.countries[i].n_troops_first = world_Data.countries[i].n_troops;

            if(world_Data.countries[i].name == "Brazil")
            {
                //world_Data.countries[i].sprite = sprite_Brasil;
                //world_Data.countries[i].text = text_Brasil;

                //Debug.Log(GameObject_Brasil_country.transform.Find("troops_display_Brazil").transform.Find("Hexagon_Back"));

                world_Data.countries[i].sprite = GameObject_Brasil_country.transform.Find("troops_display_Brazil").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Brasil_country.transform.Find("troops_display_Brazil").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Brazil", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Argentina")
            {
                world_Data.countries[i].sprite = GameObject_Argentina_country.transform.Find("troops_display_Argentina").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Argentina_country.transform.Find("troops_display_Argentina").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Argentina", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Venezuela")
            {
                world_Data.countries[i].sprite = GameObject_Venezuela_country.transform.Find("troops_display_Venezuela").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Venezuela_country.transform.Find("troops_display_Venezuela").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Venezuela", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Peru")
            {
                world_Data.countries[i].sprite = GameObject_Peru_country.transform.Find("troops_display_Peru").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Peru_country.transform.Find("troops_display_Peru").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Peru", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Alaska")
            {
                world_Data.countries[i].sprite = GameObject_Alaska_country.transform.Find("troops_display_Alaska").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Alaska_country.transform.Find("troops_display_Alaska").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Alaska", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Northwest America")
            {
                world_Data.countries[i].sprite = GameObject_Northwest_America_country.transform.Find("troops_display_Northwest America").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Northwest_America_country.transform.Find("troops_display_Northwest America").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Northwest America", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Greenland")
            {
                world_Data.countries[i].sprite = GameObject_Greenland_country.transform.Find("troops_display_Greenland").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Greenland_country.transform.Find("troops_display_Greenland").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Greenland", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Ontario")
            {
                world_Data.countries[i].sprite = GameObject_Ontario_country.transform.Find("troops_display_Ontario").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Ontario_country.transform.Find("troops_display_Ontario").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Ontario", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Alberta")
            {
                world_Data.countries[i].sprite = GameObject_Alberta_country.transform.Find("troops_display_Alberta").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Alberta_country.transform.Find("troops_display_Alberta").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Alberta", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Western America")
            {
                world_Data.countries[i].sprite = GameObject_Western_America_country.transform.Find("troops_display_Western America").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Western_America_country.transform.Find("troops_display_Western America").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Western America", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Central America")
            {
                world_Data.countries[i].sprite = GameObject_Central_America_country.transform.Find("troops_display_Central America").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Central_America_country.transform.Find("troops_display_Central America").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Central America", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Eastern America")
            {
                world_Data.countries[i].sprite = GameObject_Eastern_America_country.transform.Find("troops_display_Eastern America").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Eastern_America_country.transform.Find("troops_display_Eastern America").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Eastern America", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Quebec")
            {
                world_Data.countries[i].sprite = GameObject_Quebec_country.transform.Find("troops_display_Quebec").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Quebec_country.transform.Find("troops_display_Quebec").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Quebec", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Skandinavia")
            {
                world_Data.countries[i].sprite = GameObject_Skandinavia_country.transform.Find("troops_display_Skandinavia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Skandinavia_country.transform.Find("troops_display_Skandinavia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Skandinavia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Western Europe")
            {
                world_Data.countries[i].sprite = GameObject_Western_Europe_country.transform.Find("troops_display_Western Europe").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Western_Europe_country.transform.Find("troops_display_Western Europe").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Western Europe", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Iceland")
            {
                world_Data.countries[i].sprite = GameObject_Iceland_country.transform.Find("troops_display_Iceland").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Iceland_country.transform.Find("troops_display_Iceland").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Iceland", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Great Britain")
            {
                world_Data.countries[i].sprite = GameObject_Great_Britain_country.transform.Find("troops_display_Great Britain").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Great_Britain_country.transform.Find("troops_display_Great Britain").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Great Britain", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Southern Europe")
            {
                world_Data.countries[i].sprite = GameObject_Southern_Europe_country.transform.Find("troops_display_Southern Europe").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Southern_Europe_country.transform.Find("troops_display_Southern Europe").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Southern Europe", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Northern Europe")
            {
                world_Data.countries[i].sprite = GameObject_Northern_Europe_country.transform.Find("troops_display_Northern Europe").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Northern_Europe_country.transform.Find("troops_display_Northern Europe").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Northern Europe", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Ukraine")
            {
                world_Data.countries[i].sprite = GameObject_Ukraine_country.transform.Find("troops_display_Ukraine").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Ukraine_country.transform.Find("troops_display_Ukraine").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Ukraine", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "North Africa")
            {
                world_Data.countries[i].sprite = GameObject_North_Africa_country.transform.Find("troops_display_North Africa").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_North_Africa_country.transform.Find("troops_display_North Africa").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("North Africa", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Egypt")
            {
                world_Data.countries[i].sprite = GameObject_Egypt_country.transform.Find("troops_display_Egypt").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Egypt_country.transform.Find("troops_display_Egypt").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Egypt", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "East Africa")
            {
                world_Data.countries[i].sprite = GameObject_East_Africa_country.transform.Find("troops_display_East Africa").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_East_Africa_country.transform.Find("troops_display_East Africa").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("East Africa", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Congo")
            {
                world_Data.countries[i].sprite = GameObject_Congo_country.transform.Find("troops_display_Congo").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Congo_country.transform.Find("troops_display_Congo").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Congo", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "South Africa")
            {
                world_Data.countries[i].sprite = GameObject_South_Africa_country.transform.Find("troops_display_South Africa").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_South_Africa_country.transform.Find("troops_display_South Africa").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("South Africa", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Madagascar")
            {
                world_Data.countries[i].sprite = GameObject_Madagascar_country.transform.Find("troops_display_Madagascar").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Madagascar_country.transform.Find("troops_display_Madagascar").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Madagascar", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Ural")
            {
                world_Data.countries[i].sprite = GameObject_Ural_country.transform.Find("troops_display_Ural").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Ural_country.transform.Find("troops_display_Ural").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Ural", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Siberia")
            {
                world_Data.countries[i].sprite = GameObject_Siberia_country.transform.Find("troops_display_Siberia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Siberia_country.transform.Find("troops_display_Siberia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Siberia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Yakutsk")
            {
                world_Data.countries[i].sprite = GameObject_Yakutsk_country.transform.Find("troops_display_Yakutsk").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Yakutsk_country.transform.Find("troops_display_Yakutsk").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Yakutsk", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Irkutsk")
            {
                world_Data.countries[i].sprite = GameObject_Irkutsk_country.transform.Find("troops_display_Irkutsk").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Irkutsk_country.transform.Find("troops_display_Irkutsk").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Irkutsk", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Kamchatka")
            {
                world_Data.countries[i].sprite = GameObject_Kamchatka_country.transform.Find("troops_display_Kamchatka").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Kamchatka_country.transform.Find("troops_display_Kamchatka").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Kamchatka", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Mongolia")
            {
                world_Data.countries[i].sprite = GameObject_Mongolia_country.transform.Find("troops_display_Mongolia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Mongolia_country.transform.Find("troops_display_Mongolia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Mongolia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "China")
            {
                world_Data.countries[i].sprite = GameObject_China_country.transform.Find("troops_display_China").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_China_country.transform.Find("troops_display_China").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("China", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "India")
            {
                world_Data.countries[i].sprite = GameObject_India_country.transform.Find("troops_display_India").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_India_country.transform.Find("troops_display_India").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("India", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Siam")
            {
                world_Data.countries[i].sprite = GameObject_Siam_country.transform.Find("troops_display_Siam").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Siam_country.transform.Find("troops_display_Siam").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Siam", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Middle East")
            {
                world_Data.countries[i].sprite = GameObject_Middle_East_country.transform.Find("troops_display_Middle East").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Middle_East_country.transform.Find("troops_display_Middle East").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Middle East", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Japan")
            {
                world_Data.countries[i].sprite = GameObject_Japan_country.transform.Find("troops_display_Japan").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Japan_country.transform.Find("troops_display_Japan").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Japan", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Afganistan")
            {
                world_Data.countries[i].sprite = GameObject_Afganistan_country.transform.Find("troops_display_Afganistan").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Afganistan_country.transform.Find("troops_display_Afganistan").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Afganistan", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Eastern Australia")
            {
                world_Data.countries[i].sprite = GameObject_Eastern_Australia_country.transform.Find("troops_display_Eastern Australia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Eastern_Australia_country.transform.Find("troops_display_Eastern Australia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Eastern Australia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Western Australia")
            {
                world_Data.countries[i].sprite = GameObject_Western_Australia_country.transform.Find("troops_display_Western Australia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Western_Australia_country.transform.Find("troops_display_Western Australia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Western Australia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Indoneasia")
            {
                world_Data.countries[i].sprite = GameObject_Indoneasia_country.transform.Find("troops_display_Indoneasia").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Indoneasia_country.transform.Find("troops_display_Indoneasia").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Indoneasia", world_Data.countries[i]);
            }
            else if(world_Data.countries[i].name == "Papua New Guinea")
            {
                world_Data.countries[i].sprite = GameObject_Papua_New_Guinea_country.transform.Find("troops_display_Papua New Guinea").transform.Find("Hexagon_Back").GetComponent<SpriteRenderer>();
                world_Data.countries[i].text = GameObject_Papua_New_Guinea_country.transform.Find("troops_display_Papua New Guinea").transform.Find("Canvas").transform.Find("Text (TMP)").GetComponent<TextMeshProUGUI>();
                countries.Add("Papua New Guinea", world_Data.countries[i]);
            }
        }

        /*Debug.Log(countries["Papua New Guinea"].n_troops);
        Debug.Log(countries["Indoneasia"].n_troops);
        Debug.Log(countries["Indoneasia"].owner);

        make_dict_turn_data(2);

        Debug.Log(countries["Papua New Guinea"].n_troops);
        Debug.Log(countries["Indoneasia"].n_troops);
        Debug.Log(countries["Indoneasia"].owner);*/

        //Debug.Log(countries["Irkutsk"].n_troops);

        //make_dict_turn_data(1);

        make_dict_turn_data(0);
        //make_dict_command_data(0,19);

        //Debug.Log(countries["Irkutsk"].n_troops);

        //Debug.Log(countries["Brazil"].n_troops);
        //Debug.Log(countries["Brazil"].n_troops_first);

        //Debug.Log(turns_data.turns[0].calls[0].name_in.GetType().ToString());
        //Debug.Log( countries[turns_data.turns[0].calls[0].name_in].n_troops );

        //Debug.Log(sprite_Papua_New_Guinea.position);

    }

    void Update()
    {
        foreach (KeyValuePair<string,country> c in countries)
        {
            c.Value.text.text = c.Value.n_troops.ToString();

            if(c.Value.owner == 1)
            {
                c.Value.sprite.color = Player_1_Color;
            }
            else
            {
                c.Value.sprite.color = Player_2_Color;
            }
        }

        

        /*timer += Time.deltaTime;
        //seconds = timer % 60;

        if( timer >= 5.0f)
        {
            Debug.Log(timer % 60);
            timer -= timer;
        }*/
        
    }
}
