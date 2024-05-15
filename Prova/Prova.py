def feed(height, width, area_fence):

        area_animale: float = width * height

        if height * 2 / 100 * width * 2 / 100 <= area_fence:
            
            # sottrarre l'area occupata dall'area residua
            area_fence = area_fence - ((height * 0.02) * width * 1.02) + ((width * 0.02) * height * 1.02)
                                                #2% dell'altezza*il totale della base INCREMENTATA    per      2%larghezza*il totale dell'altezza INCREMENTATA               

            height = height * 1.02
            width = width * 1.02
            health = health * 1.01


