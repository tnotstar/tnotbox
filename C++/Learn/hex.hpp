//
// hex.hpp: an implementation of the game of HEX
//

#ifndef HEX_HPP_INCLUDED
#define HEX_HPP_INCLUDED

#include <cctype>
#include <string>
#include <sstream>
#include <iostream>

#include "graph.hpp"

namespace hex {

    /**
     * An enumerator class for the colors of HEX.
     */
    enum class color {
        UNKNOWN = 0,
        BLUE,
        RED
    };

    /**
     *  Stores a cell from the HEX board.
     */
    class cell {
    public:
        /// A type declaration for the cell's indexes.
        typedef size_t index_type;

        /// A type declaration for the cell's color.
        typedef color color_type;

        /**
         * Builds an instance of the class cell, from a given tuple of
         * relative coordinates `(x, y)`.
         */
         cell(const index_type& x=0, const index_type& y=0,
                const color_type& the_color=color::UNKNOWN) :
            _x(x), _y(y), _color(the_color)
        {}

        /**
         * Builds an instance of the class cell, from a given label string.
         */
        cell(const std::string& label,
                const color_type& the_color=color::UNKNOWN) :
            _x(0), _y(0), _color(the_color)
        {
            if (label.size() > 1) {
                char ch = std::toupper(label.c_str()[0]);
                if ('A' <= ch && ch <= 'Z')
                    _x = static_cast<index_type>(ch - 'A');
            }

            if (label.size() > 2) {
                std::stringstream buffer(label.c_str() + 1);
                buffer >> _y;
            }
        }

        /**
         * Assigns a new color to the cell.
         */
        void
        set_color(const color_type& the_color) {
            _color = the_color;
        }

        /**
         * Returns the horizontal coordinate of this cell.
         */
        index_type
        get_x() const {
            return _x;
        }

        /**
         * Returns the vertical coordinate of this cell.
         */
        index_type
        get_y() const {
            return _y;
        }

        /**
         * Returns the current color of this cell.
         */
        color_type
        get_color() const {
            return _color;
        }

        /**
         * Returns the label associated with this cell.
         */
        std::string
        get_label() const {
            std::stringstream buffer;
            buffer << static_cast<char>('A' + _x - 1) << _y;
            return buffer.str();
        }

    private:
        // A value with the horizontal coordinate.
        index_type _x;

        // A value with the vertical coordinate.
        index_type _y;

        // A value with the color of the cell.
        color_type _color;
    };

    /**
     * Stores the board for the HEX game.
     */
    class board
    {
    public:
        /// A type declaration for the graph representation of this board.
        typedef graph::sparse_graph<std::string, cell, double> graph_type;

        /// A type declaration for the size of the board.
        typedef typename graph_type::size_type size_type;

        /// A type declaration for the index of a cell in the board.
        typedef typename cell::index_type index_type;

        /// A type declaration for the color of a cell in the board.
        typedef typename cell::color_type color_type;

        /**
         * This is the default constructor for objects of this type.
         *
         * Explicit is used here, to avoid implicit conversion from values
         * of type `size_type`.
         */
        explicit board(size_type size=11) :
            _size(size), _graph(size*size)
        {
            for (size_type row = 1; row <= _size; ++row) {
                for (size_type col = 1; col <= _size; ++col) {
                    cell the_cell(row, col);
                    _graph.add_node(the_cell.get_label(), the_cell);
                }
            }
        }

        /**
         * Returns the size of this board.
         */
        size_type
        size() const {
            return _size;
        }

        /**
         * Returns the color from given cell in the board.
         */
        color_type
        color_at(const index_type& x, const index_type& y) const {
            cell the_cell(x, y);
            if (!exists(the_cell))
                return color::UNKNOWN;

            auto label = the_cell.get_label();
            return _graph.value_at(label).get_color();
        }


        /**
         * Checks if given cell exists on the board.
         */
        bool
        exists(const cell& the_cell) const {
            auto label = the_cell.get_label();
            return _graph.exists(label);
        }

        /**
         * Checks if given move it's valid.
         */
        bool
        is_valid(const cell& the_cell) const {
            if (!exists(the_cell))
                return false;

            auto value = _graph.value_at(the_cell.get_label());
            return value.get_color() == color::UNKNOWN;
        }

        /**
         * Checks if there's a winner.
         */
        bool
        has_winner() const {
            return true;
        }

    private:
        // Stores the size of the board.
        size_type _size;

        // Stores the graph of the board.
        graph_type _graph;

        // A friend method to dump the content of the board.
        friend std::ostream&
        operator <<(std::ostream& out, const board& the_board);
    };

    // Dumps the current contents from given board.
    std::ostream&
    operator <<(std::ostream& out, const board& the_board) {

        out << std::endl << std::endl;
        for (board::size_type col = 0; col < the_board.size(); ++col)
            out << "   " << static_cast<char>('A' + col);
        out << std::endl;

        int indent = 0;
        for (board::size_type row = 1; row <= the_board.size(); ++row) {
            for (int i = 0; i < indent; ++i)
                out << "  ";

            out << row;
            for (board::size_type col = 1; col <= the_board.size(); ++col) {
                color the_color = the_board.color_at(row, col);
                switch (the_color) {
                case color::BLUE:
                    out << "  X ";
                    break;
                case color::RED:
                    out << "  O ";
                    break;
                default:
                    out << "  . ";
                }

            }
            out << row << std::endl;

            indent++;
        }

        for (int i = 0; i < indent; ++i)
            out << "  ";

        for (board::size_type col = 0; col < the_board.size(); ++col)
            out << "   " << static_cast<char>('A' + col);
        out << std::endl;

        return out;
    }

    /// A forward declaration for the class `game`.
    class game;

    /**
     * Encapsulates the logic of a human HEX's player.
     */
    class player {
    public:
        /// A type declaration for the player's color.
        typedef color color_type;

        /**
         * Builds an instance of the player class with mandatory
         * color value and game pointer.
         */
        player(const color_type& the_color) :
            _color(the_color)
        {}

        /**
         * Returns the player's color value.
         */
        color_type
        get_color() const {
            return _color;
        }

        /**
         * A method to calculate the next player's move.
         */
        cell
        next_move() {
            std::cout << "Enter location: ";

            std::string input;
            std::cin >> input;

            return cell(input);
        }

    protected:
        // An enum value with the color of this player.
        color_type _color;
    };

    /**
     * Stores a game of HEX, with its board and its two players.
     */
    class game {
    public:
        /// A type declaration for the size of the board.
        typedef typename board::size_type size_type;

        /// A type declaration for the game's board.
        typedef board board_type;

        /// A type declaration for the game's players.
        typedef player player_type;

        /**
         * A constructor to initialize the board with given dimensions, and
         * to inject both players at build time.
         */
        game(const size_type& size) :
            _board(size), _blue(color::BLUE), _red(color::RED)
        {}

        /**
         * Executes the game of HEX!
         */
        void
        play() {
            std::cout << "Playing with an " << _board.size() << "x" << _board.size()
                          << " board." << std::endl
                      << "------------------------------------------------------------" << std::endl
                      << "Board (no moves)"                                             << std::endl
                      << _board                                                         << std::endl
                      << "------------------------------------------------------------" << std::endl
                      << "Blue human goes first"                                        << std::endl
                      << "------------------------------------------------------------" << std::endl;

            std::array<player_type *, 2> players = {&_blue, &_red};
            int turn = 0;

            do {
                // Ask the next move from the current player.
                cell move = players[turn % 2]->next_move();
                while (!_board.is_valid(move)) {
                    move = players[turn % 2]->next_move();
                }

                // Calculates the next player.
                turn++;
            } while(!_board.has_winner());

        }

    private:
        // This is the board for the game.
        board_type _board;

        // An instance to store the blue player.
        player_type _blue;

        // An instance to store the blue player.
        player_type _red;
    };

} //namespace hex

#endif // HEX_HPP_INCLUDED
